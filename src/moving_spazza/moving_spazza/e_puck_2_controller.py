import rclpy

from rosgraph_msgs.msg import Clock 
from spazza_interfaces.msg import Position
from ros2_bdi_interfaces.msg import Belief

import math

ADMISSIBLE_ERROR = 0.03
ADMISSIBLE_ERROR_POSITION = 0.003
MAX_ANGULAR_SPEED = 0.05
MAX_LINEAR_SPEED = 6.28
MIN_LINEAR_SPEED = 2.0
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
N_TILES = 7
LEFT = 1
RIGHT = -1
MOVE_RATE = 360

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.rotating = False
        self.moving = False
        self.current_tile_target = -1  # initially no target
        self.target_x = 0.0
        self.target_y = 0.0
        self.target_theta = 0.0
        self.diff_theta = 0.0
        self.distance = 0.0
        self.theta = 0.0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.__time = 0

        self.__loop = [28, 21, 22, 23, 24, 31, 38, 45, 44, 43, 42, 35]
        self.__index_loop = 1

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')

        self.position_subscription = self.__node.create_subscription(
            Position,
            'robot_position_2',
            self.position_callback,
            32
        )

        self.clock_subscription = self.__node.create_subscription(
            Clock,
            'clock',
            self.clock_callback,
            10
        )

        self.add_belief_publisher = self.__node.create_publisher(
            Belief, 'e_puck/add_belief', 4
        )
        self.delete_belief_publisher = self.__node.create_publisher(
            Belief, 'e_puck/del_belief', 4
        )

    # called at every time step of the simulation
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        if self.rotating:
            self.diff_theta = abs(self.target_theta - self.theta)
            # stop rotating
            if self.diff_theta < ADMISSIBLE_ERROR:
                self.stop_motor()
                self.rotating = False
                self.move_robot_forward()
                self.moving = True
                return
            self.rotate_robot(self.rotational_direction)

        if self.moving:
            self.distance = (self.target_y - self.y) ** 2 + \
                (self.target_x - self.x) ** 2
            # stop moving forwards
            if self.distance < ADMISSIBLE_ERROR_POSITION:
                self.stop_motor()
                self.moving = False     
                return
            self.move_robot_forward()

    def clock_callback(self, msg):
        if self.__time != msg.clock.sec:
            if self.__time % MOVE_RATE == 0:
                self.move_callback(self.__loop[self.__index_loop])
                self.update_bel_set_during_transition()
                self.__index_loop = self.__index_loop + 1 if self.__index_loop < len(self.__loop) - 1 else 0

            self.__time += 1

    def update_bel_set_during_transition(self):
        belief = Belief()
        belief.name = 'walkable'
        belief.pddl_type = 2
        belief.params = ['t' + str(self.__loop[self.__index_loop])]
        self.delete_belief_publisher.publish(belief) #tile I'm moving to isn't walkable anymore


        old_tile_index = self.__index_loop - 1 if self.__index_loop != 0 else len(self.__loop) - 1
        belief.params = ['t' + str(self.__loop[old_tile_index])]
        self.add_belief_publisher.publish(belief) #tile I am coming from is now walkable

    # callback upon receiving move message)
    def move_callback(self, msg):
        if (msg != self.current_tile_target):
            self.current_tile_target = msg

            self.rotational_direction = self.calculate_rotational_direction(
                self.theta, self.target_theta)
            self.rotate_robot(self.rotational_direction)

            self.__node.get_logger().info('moving to t%d' %(msg))
            self.current_tile_target = msg

            self.target_x = self.get_x_coordinate_from_tile_number(msg)
            self.target_y = self.get_y_coordinate_from_tile_number(msg)
            delta_y = self.target_y - self.y
            delta_x = self.target_x - self.x

            if delta_x == 0:
                self.target_theta = math.pi / 2 if delta_y > 0 else -math.pi / 2
            elif delta_y == 0:
                self.target_theta = 0.0 if delta_x > 0 else math.pi
            else:
                theta = math.fabs(math.atan(delta_y / delta_x)) if self.target_y > self.y else math.fabs(
                    math.atan(delta_x / delta_y))  # angle between robot and target
                if self.target_y > self.y:
                    self.target_theta = theta if self.target_x > self.x else math.pi - theta
                else:
                    self.target_theta = -math.pi / 2 - \
                        theta if self.target_x < self.x else -math.pi / 2 + theta

            self.rotating = True
            self.__left_motor.setPosition(float('inf'))
            self.__right_motor.setPosition(float('inf'))

            # not actual dist to make computation lighter
            self.distance = delta_x ** 2 + delta_y ** 2

            self.rotational_direction = self.calculate_rotational_direction(
                self.theta, self.target_theta)
            self.rotate_robot(self.rotational_direction)

    def move_robot_forward(self):
        self.__left_motor.setVelocity(
            max(MAX_LINEAR_SPEED * self.distance, MIN_LINEAR_SPEED))
        self.__right_motor.setVelocity(
            max(MAX_LINEAR_SPEED * self.distance, MIN_LINEAR_SPEED))

    def stop_motor(self):
        self.__left_motor.setVelocity(0)
        self.__right_motor.setVelocity(0)

    def rotate_robot(self, direction):
        self.__left_motor.setVelocity(-direction * MAX_ANGULAR_SPEED)
        self.__right_motor.setVelocity(direction * MAX_ANGULAR_SPEED)

    # update robot position
    def position_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.z = msg.z
        self.theta = msg.theta

    # x coordinates given tile number
    @staticmethod
    def get_x_coordinate_from_tile_number(i):
        distance_from_margin = i % N_TILES * TILE_SIZE + \
            HALF_TILE_SIZE  # distance from the top margin
        half_board = (N_TILES // 2) * TILE_SIZE + \
            HALF_TILE_SIZE  # half of the board
        return -(half_board - distance_from_margin)

    # y coordinates given tile number
    @staticmethod
    def get_y_coordinate_from_tile_number(i):
        # distance from the left hand side margin
        distance_from_margin = (i // N_TILES) * TILE_SIZE + HALF_TILE_SIZE
        half_board = (N_TILES // 2) * TILE_SIZE + \
            HALF_TILE_SIZE  # half of the board
        return half_board - distance_from_margin

    @staticmethod
    def calculate_rotational_direction(robot_angle, target_angle):
        # if (robot_angle >= 0 and target_angle >= 0) or (robot_angle < 0 and target_angle < 0):
        #     return LEFT if robot_angle < target_angle else RIGHT

        # if robot_angle >= 0 and target_angle <= 0:
        #     return RIGHT if (robot_angle - target_angle) < (2 * math.pi + target_angle - robot_angle) else LEFT

        # return LEFT if (robot_angle - target_angle) < (2 * math.pi + target_angle - robot_angle) else RIGHT
        return LEFT
