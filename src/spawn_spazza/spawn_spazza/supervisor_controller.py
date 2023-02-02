import rclpy
from rclpy.node import Node

from rosgraph_msgs.msg import Clock
from builtin_interfaces.msg import Time
from geometry_msgs.msg import Point
from spazza_interfaces.msg import Position
from std_msgs.msg import Int16
from ros2_bdi_interfaces.msg import Belief

import random

MOVE_BOX_TIME = 5
ADD_GARBAGE_TIME = 10
# how often the position is refreshed, in seconds
ROBOT_POSITION_UPDATE_RATE = 0.001
N_TILES = 7
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
SPAWN_RATE = 800
ARR_SIZE = 256

'''
A duck gets spawned every SPAWN_RATE seconds and it never disappears
'''

class SupervisorController:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__time = 0

        self.__e_puck = self.__robot.getFromDef('e_puck')
        self.__duck_count = 0
        self.__duck_refs = [None] * ARR_SIZE
        self.__duck_tiles = [None] * ARR_SIZE
        self.__occ_tiles = {1, 8, 10, 11, 12, 29, 30, 32, 36, 37, 39}
        self.__first_duck_done = False

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')
        self.__children_field = self.__robot.getRoot().getField('children')

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
        self.new_garbage_belief_publisher = self.__node.create_publisher(
            Belief, 'e_puck/add_belief', 4)

    # called at every time step of the simulation
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

    # every time the clock goes forward this function is called
    def clock_callback(self, msg):
        if self.__time != msg.clock.sec:
            if self.__time % SPAWN_RATE == 0:
                #spawn duck
                new_position = random.randint(0, N_TILES * N_TILES - 1)
                while new_position in self.__occ_tiles:
                    new_position = random.randint(0, N_TILES * N_TILES - 1)
                self.__occ_tiles.add(new_position)

                self.__children_field.importMFNodeFromString(-1, 'DEF DUCK' + str(
                    self.__duck_count) + ' RubberDuck {translation ' +
                    str(self.get_x_coordinate_from_tile_number(new_position)) + ' ' +
                    str(self.get_y_coordinate_from_tile_number(new_position)) + ' 0 scale 0.5}')
                self.__duck_refs[self.__duck_count] = self.__robot.getFromDef('DUCK' + str(self.__duck_count))
                self.__duck_tiles[self.__duck_count] = new_position

                #push belief that there is a new duck which will trigger the reactive rule to add a new desire to retireve it
                belief = Belief()
                belief.name = 'at_gar'
                belief.pddl_type = 2
                belief.params = ['g' + str(self.__duck_count), 't' + str(new_position)]
                self.new_garbage_belief_publisher.publish(belief)

                self.__node.get_logger().info('New duck spawned at tile nr. %d' %(new_position))

                #TODO: push the belief that this particular tile is not walkable
                
                self.__duck_count += 1
            self.__time += 1

    def robot_position_timer_callback(self):
        position = self.__e_puck.getPosition()
        orientation = self.__e_puck.getField('rotation')  # get angle
        orientation_values = orientation.getSFRotation()

        if orientation_values[2] < 0:
            new_values = [orientation_values[0],
                          orientation_values[1], 1.0, orientation_values[3]]
            orientation.setSFRotation(new_values)

        msg = Position()
        msg.x = position[0]
        msg.y = position[1]
        # msg.z = orientation_values[2]
        msg.theta = orientation_values[3]

        self.robot_position_publisher.publish(msg)

    def pickup_garbage_callback(self, msg):
        self.__node.get_logger().info('I was told to remove the duck number %d' %(msg.data))
        if self.__first_duck_done == False:
            self.__duck_refs[0].getField('translation').setSFVec3f([20, 20, 20])
            self.__duck_tiles[0] = -1
        else:
            self.__duck_refs[msg.data].remove()

    def putdown_garbage_callback(self, msg):
        if self.__first_duck_done == False:
            self.__first_duck_done = True
            self.__duck_refs[0].getField('translation').setSFVec3f([-0.496798, 0.97926, 0])

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
