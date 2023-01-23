import rclpy
import math

from spazza_interfaces.msg import Position
from spazza_interfaces.msg import Pose
from geometry_msgs.msg import Point
from std_msgs.msg import Int16


HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025
TIME_STEP = 64
MAX_SPEED = 6.28
PI = 3.14159
ADMISSIBLE_ERROR = 0.01
ROTATIONAL_SPEED = 0.05
LINEAR_SPEED = 0.15
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
N_TILES = 7


class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.rotating = False
        self.moving = False

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

        #move receives the tile number where to move to
        self.move_subscription = self.__node.create_subscription(
            Int16,
            'move',
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
        if self.rotating and abs(self.target_theta - self.theta) < ADMISSIBLE_ERROR:
            self.__left_motor.setVelocity(0)
            self.__right_motor.setVelocity(0)
            self.rotating = False
            self.moving = True
            self.move_after_rotation_is_complete()

        # stop moving forward
        if self.moving and abs(self.x - self.target_x) < ADMISSIBLE_ERROR and abs(self.y - self.target_y) < ADMISSIBLE_ERROR:
            self.__left_motor.setVelocity(0)
            self.__right_motor.setVelocity(0)
            self.moving = False

    # callback upon receiving move message
    def move_callback(self, msg):
        self.__node.get_logger().info('I was told to move to tile number %d' % (msg.data))

        # coordinates target
        self.target_x = self.tile_x(msg.data)
        self.target_y = self.tile_y(msg.data)

        self.__node.get_logger().info('target_x: %f, target_y: %f' %(self.target_x, self.target_y))

        # calculating the angle of the objective w.r.t. the robot's position
        self.target_theta = self.compute_target_theta(self.x, self.y, self.target_x, self.target_y)
        self.__node.get_logger().info('target_theta: %f' %(self.target_theta))

        # deciding whether to turn left or right
        go_left = True if self.target_theta > 0 else False

        # adjusting the robot's rotation
        self.__left_motor.setPosition(float('inf'))
        self.__right_motor.setPosition(float('inf'))

        if not go_left:
            self.__left_motor.setVelocity(-ROTATIONAL_SPEED * MAX_SPEED)
            self.__right_motor.setVelocity(ROTATIONAL_SPEED * MAX_SPEED)
        else:
            self.__left_motor.setVelocity(ROTATIONAL_SPEED * MAX_SPEED)
            self.__right_motor.setVelocity(-ROTATIONAL_SPEED * MAX_SPEED)
        self.rotating = True

    #after rotation is complete this function, which moves the robot forwards, is called
    def move_after_rotation_is_complete(self):
        self.__left_motor.setVelocity(LINEAR_SPEED * MAX_SPEED)
        self.__right_motor.setVelocity(LINEAR_SPEED * MAX_SPEED)

    # update robot position
    def position_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta

    # x coordinates given tile number
    @staticmethod
    def tile_x(i):
        distance_from_margin = i % N_TILES * TILE_SIZE + HALF_TILE_SIZE #distance from the top margin
        half_board = (N_TILES // 2) * TILE_SIZE + HALF_TILE_SIZE #half of the board
        return -(half_board - distance_from_margin)

    # y coordinates given tile number
    @staticmethod
    def tile_y(i):
        distance_from_margin = (i // N_TILES) * TILE_SIZE + HALF_TILE_SIZE #distance from the left hand side margin
        half_board = (N_TILES // 2) * TILE_SIZE + HALF_TILE_SIZE #half of the board
        return half_board - distance_from_margin

    @staticmethod
    def compute_target_theta(x, y, target_x, target_y):
        theta = None
        if (x < target_x):
            theta = math.atan(abs(y - target_y) / abs(x - target_x)) if x != target_x else 0
        else:
            theta = math.atan(abs(x - target_x) / abs(y - target_y)) + PI / 2 if y != target_y else 0
        
        if (y > target_y):
            theta = -theta

        return theta

