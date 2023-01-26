import rclpy
from rclpy.node import Node

from rosgraph_msgs.msg import Clock
from builtin_interfaces.msg import Time
from geometry_msgs.msg import Point
from spazza_interfaces.msg import Position
from std_msgs.msg import Int16

MOVE_BOX_TIME = 5
ADD_GARBAGE_TIME = 10
ROBOT_POSITION_UPDATE_RATE = 0.01 #how often the position is refreshed, in seconds

class SupervisorController:
    def init(self, webots_node, properties):    
        self.__robot = webots_node.robot
        self.__time = 0
        self.__path_blocked = False
        self.__second_trash_positioned = False

        self.__box = self.__robot.getFromDef('magic_box')
        self.__box2 = self.__robot.getFromDef('magic_box2')
        self.__trash = self.__robot.getFromDef('TRASH_1')
        self.__trash2 = self.__robot.getFromDef('TRASH_2')
        self.__e_puck = self.__robot.getFromDef('e_puck')

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')

        self.clock_subscription = self.__node.create_subscription(
            Clock,
            'clock',
            self.clock_callback,
            10
        )
        self.clock_subscription  # prevent unused variable warning

        self.robot_position_publisher = self.__node.create_publisher(
            Position, 'robot_position', 32)
        self.robot_position_timer = self.__node.create_timer(
            ROBOT_POSITION_UPDATE_RATE, self.robot_position_timer_callback)
        
        self.pickup_garbage_subscription = self.__node.create_subscription(
            Int16,
            'e_puck/pickup',
            self.pickup_garbage_callback,
            4
        )
        self.putdown_garbage_subscription = self.__node.create_subscription(
            Int16,
            'e_puck/putdown',
            self.putdown_garbage_callback,
            4
        )

    # called at every time step of the simulation
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

    # every time the clock goes forward this function is called
    def clock_callback(self, msg):
        return
        # if self.__time != msg.clock.sec:
        #     self.__time += 1

        #     # move the boxes to block/free the path to the garbage every MOVE_BOX_TIME seconds
        #     if self.__time % MOVE_BOX_TIME == 0:
        #         translationField = self.__box.getField('translation')
        #         translationField2 = self.__box2.getField('translation')

        #         if self.__path_blocked:
        #             new_value = [5, 5, 5]
        #             new_value2 = [6, 6, 6]
        #         else:
        #             new_value = [0.291, -0.292, 0.15]
        #             new_value2 = [0.867, -0.296, 0.145]

        #         self.__path_blocked = not self.__path_blocked
        #         translationField.setSFVec3f(new_value)
        #         translationField2.setSFVec3f(new_value2)

            # # add a second bottle to the simulation after ADD_GARBAGE_TIME seconds
            # if self.__time % ADD_GARBAGE_TIME == 0 and self.__second_trash_positioned == False:
            #     translationFieldTrash = self.__trash2.getField('translation')
            #     new_value = [-0.298, -0.873, -0.01]
            #     translationFieldTrash.setSFVec3f(new_value)
            #     self.__second_trash_positioned = True

    #publishes into topic 'robot position' the position of the robot
    #spazza_interfaces/msg/Position
    def robot_position_timer_callback(self):
        position = self.__e_puck.getPosition()
        orientation = self.__e_puck.getField('rotation') #get angle
        orientation_values = orientation.getSFRotation()
        
        if orientation_values[2] < 0:
            new_values = [orientation_values[0], orientation_values[1], 1.0, orientation_values[3]]
            orientation.setSFRotation(new_values) 

        msg = Position()
        msg.x = position[0]
        msg.y = position[1]
        #msg.z = orientation_values[2]
        msg.theta = orientation_values[3]

        self.robot_position_publisher.publish(msg)

    def pickup_garbage_callback(self, msg):
        if msg.data == 1:
            position = self.__trash.getField('translation')
        else:
            position = self.__trash2.getField('translation')
        new_values = [20, 20, 20]
        position.setSFVec3f(new_values)

    def putdown_garbage_callback(self, msg):
        if msg.data == 1:
            position = self.__trash.getField('translation')
        else:
            position = self.__trash2.getField('translation')
        new_values = [-0.496798, 0.97926, 0]
        position.setSFVec3f(new_values)

        
