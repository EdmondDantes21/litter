import rclpy

from spazza_interfaces.msg import Position
from std_msgs.msg import Int16, Empty

import math

HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025
TIME_STEP = 64
MAX_SPEED = 6.28
PI = 3.14159
ADMISSIBLE_ERROR = 0.03
ADMISSIBLE_ERROR_POSITION = 0.003
MAX_ANGULAR_SPEED = 0.1
MAX_LINEAR_SPEED = 6.28
MIN_LINEAR_SPEED = 2.0
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
N_TILES = 7
LEFT = 1
RIGHT = -1


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

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')

        self.move_subscription = self.__node.create_subscription(
            Int16,
            'e_puck/move',
            self.move_callback,
            10
        )
        self.position_subscription = self.__node.create_subscription(
            Position,
            'robot_position',
            self.position_callback,
            32
        )
        self.move_completed_publisher = self.__node.create_publisher(
            Empty,
            'e_puck/move_completed',
            4
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
                # telling ROS2-BDI that the movement is finished
                msg = Empty()
                self.move_completed_publisher.publish(msg)
                return
            self.move_robot_forward()

    # callback upon receiving move message
    def move_callback(self, msg):
        if (msg.data != self.current_tile_target):
            self.current_tile_target = msg.data
            self.__node.get_logger().info('moving to tile nr. %d' % (msg.data))

            self.target_x = self.get_x_coordinate_from_tile_number(msg.data)
            self.target_y = self.get_y_coordinate_from_tile_number(msg.data)
            delta_y = self.target_y - self.y
            delta_x = self.target_x - self.x
            #self.__node.get_logger().info('delta_x: %f, delta_y: %f' % (delta_x, delta_y))

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

            #self.__node.get_logger().info('target_theta: %f' % self.target_theta)

            self.rotating = True
            self.__left_motor.setPosition(float('inf'))
            self.__right_motor.setPosition(float('inf'))

            # not actual dist to make computation lighter
            self.distance = delta_x ** 2 + delta_y ** 2

            self.rotational_direction = self.calculate_rotational_direction(
                self.theta, self.target_theta)
            self.rotate_robot(self.rotational_direction)

    # after rotation is complete this function, which moves the robot forwards, is called
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
