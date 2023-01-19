import rclpy
from geometry_msgs.msg import Twist

HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025
TIME_STEP = 64
MAX_SPEED = 6.28

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')

        self.__left_motor.setPosition(float('inf'))
        self.__left_motor.setVelocity(0)

        self.__right_motor.setPosition(float('inf'))
        self.__right_motor.setVelocity(0)

        self.__ps = []
        self.__psNames = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
        for i in range(8):
            self.__ps.append(self.__robot.getDevice(self.__psNames[i]))
            self.__ps[i].enable(TIME_STEP)

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')
    
    #called at every time step of the simulation
    #spins once, then sets the forward speed and angular speed from the Twist message
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        psValues = []
        for i in range(8):
            psValues.append(self.__ps[i].getValue())

        # detect obstacles
        right_obstacle = psValues[0] > 80.0 or psValues[1] > 80.0 or psValues[2] > 80.0
        left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0 or psValues[7] > 80.0

        # initialize motor speeds at 50% of MAX_SPEED.
        leftSpeed  = 0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
        # modify speeds according to obstacles
        if left_obstacle:
            # turn right
            leftSpeed  = 0.5 * MAX_SPEED
            rightSpeed = -0.5 * MAX_SPEED
        elif right_obstacle:
            # turn left
            leftSpeed  = -0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
        # write actuators inputs
        self.__left_motor.setVelocity(leftSpeed)
        self.__right_motor.setVelocity(rightSpeed)
