import rclpy
from geometry_msgs.msg import Twist
from controller import Robot, DistanceSensor, Motor


HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025
TIME_STEP = 64

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')
        self.__ds0 = self.__robot.getDevice('ds0')
        self.__ds1 = self.__robot.getDevice('ds1')

        self.__ds0.enable(TIME_STEP)
        self.__ds1.enable(TIME_STEP)

        self.__left_motor.setPosition(float('inf'))
        self.__left_motor.setVelocity(0)

        self.__right_motor.setPosition(float('inf'))
        self.__right_motor.setVelocity(0)

        self.__target_twist = Twist()

        rclpy.init(args=None)
        self.__node = rclpy.create_node('my_robot_driver')
        self.__node.create_subscription(Twist, 'cmd_vel', self.__cmd_vel_callback, 1)
        #cmd_vel will handle Twist messages

    #when a Twist message is received from the cmd_vel subscription, this function is called
    #it just sets the robot's twist to the received twist
    def __cmd_vel_callback(self, twist):   
        self.__target_twist = twist

    #called at every time step of the simulation
    #spins once, then sets the forward speed and angular speed from the Twist message
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        forward_speed = self.__target_twist.linear.x
        angular_speed = self.__target_twist.angular.z

        command_motor_left = (forward_speed - angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS
        command_motor_right = (forward_speed + angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS

        self.__left_motor.setVelocity(command_motor_left)
        self.__right_motor.setVelocity(command_motor_right)

        #checking the distance sensors
