import rclpy

from spazza_interfaces.msg import Position
from spazza_interfaces.msg import Pose
from std_msgs.msg import Int16

import math

HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025
TIME_STEP = 64
MAX_SPEED = 6.28
PI = 3.14159
ADMISSIBLE_ERROR = 0.01
ANGULAR_SPEED = 0.04
LINEAR_SPEED = 0.2
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
N_TILES = 7

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.rotating = False
        self.moving = False
        self.current_tile_target = -1  # initially no target
        self.target_x = 0.0 
        self.target_y = 0.0
        self.target_theta = 0.0

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')

        self.__ps = []
        self.__psNames = ['ps0', 'ps1', 'ps2',
                          'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
        for i in range(8):
            self.__ps.append(self.__robot.getDevice(self.__psNames[i]))
            self.__ps[i].enable(TIME_STEP)

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')

        # move receives the tile number where to move to
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

    # called at every time step of the simulation
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        # stop rotating
        if self.rotating and abs(self.theta - self.target_theta) < ADMISSIBLE_ERROR and abs(self.target_theta - self.theta) < ADMISSIBLE_ERROR:
            self.stop_motor()
            self.rotating = False
            self.move_robot()
            self.moving = True

        # stop moving forward
        if self.moving and abs(self.x - self.target_x) < ADMISSIBLE_ERROR and abs(self.y - self.target_y) < ADMISSIBLE_ERROR:
            self.stop_motor()
            self.moving = False

    # callback upon receiving move message
    def move_callback(self, msg):
        if (msg.data != self.current_tile_target):
            self.current_tile_target = msg.data
            self.__node.get_logger().info('I was told to move to tile number %d' % (msg.data))

            self.target_x = self.get_x_coordinate_from_tile_number(msg.data) 
            self.target_y = self.get_y_coordinate_from_tile_number(msg.data)
            delta_y = self.target_y - self.y
            delta_x = self.target_x - self.x
            theta = math.fabs(math.atan(delta_y / delta_x)) if self.target_y > self.y else math.fabs(math.atan(delta_x / delta_y)) #angle between robot and target

            if self.target_y > self.y:
                self.target_theta = theta if self.target_x > self.x  else math.pi - theta
            else:
                self.target_theta = -math.pi / 2 - theta if self.target_x < self.x else -math.pi / 2 + theta
            self.__node.get_logger().info('target_x: %f, target_y: %f' %(self.target_x, self.target_y))
            self.__node.get_logger().info('target_theta: %f' %(self.target_theta))

            self.rotating = True
            self.__left_motor.setPosition(float('inf'))
            self.__right_motor.setPosition(float('inf'))

            # turning motors left
            self.__left_motor.setVelocity(ANGULAR_SPEED * MAX_SPEED)
            self.__right_motor.setVelocity(-ANGULAR_SPEED * MAX_SPEED)

    # after rotation is complete this function, which moves the robot forwards, is called
    def move_robot(self):
        self.__left_motor.setVelocity(LINEAR_SPEED * MAX_SPEED)
        self.__right_motor.setVelocity(LINEAR_SPEED * MAX_SPEED)

    def stop_motor(self):
        self.__left_motor.setVelocity(0)
        self.__right_motor.setVelocity(0)

    # update robot position
    def position_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
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
