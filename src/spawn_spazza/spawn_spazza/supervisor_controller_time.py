import rclpy
from rclpy.node import Node

from rosgraph_msgs.msg import Clock
from spazza_interfaces.msg import Position
from std_msgs.msg import Int16
from ros2_bdi_interfaces.msg import Belief, Desire

import random

# how often the position is refreshed, in seconds
ROBOT_POSITION_UPDATE_RATE = 0.001
N_TILES = 7
TILE_SIZE = 0.29  # size of the physical square in the simulation
HALF_TILE_SIZE = TILE_SIZE / 2
SPAWN_RATE = 700
LIFE_SPAN = 500
ARR_SIZE = 256

'''
A duck gets spawned every SPAWN_RATE seconds and it disappears after LIFE_SPAN seconds if it doesnt get caught
'''

class SupervisorController:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__time = 0

        self.__e_puck = self.__robot.getFromDef('e_puck')
        self.__duck_count = 0
        self.__duck_refs = [None] * ARR_SIZE
        self.__duck_tiles = [None] * ARR_SIZE
        # time left (in seconds) before this duck disappears
        self.__duck_time_left = [None] * ARR_SIZE
        self.__duck_catched = [False] * ARR_SIZE
        self.__occ_tiles = {1, 8, 10, 11, 12, 29, 30, 32, 36, 37, 39}
        self.__first_duck_done = False
        self.__robot_position = 8

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
        self.new_belief_publisher = self.__node.create_publisher(
            Belief, '/e_puck/add_belief', 4)
    
        self.delete_belief_publisher = self.__node.create_publisher(
            Belief, '/e_puck/del_belief', 4)
        
        self.move_subscription = self.__node.create_subscription(
            Int16,
            'e_puck/move',
            self.move_callback,
            10
        )

    # called at every time step of the simulation
    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

    # every time the clock goes forward this function is called
    def clock_callback(self, msg):
        if self.__time != msg.clock.sec:
            self.remove_elapsed_ducks()

            if self.__time % SPAWN_RATE == 0:
                self.spawn_new_duck()
            self.__time += 1

    def spawn_new_duck(self):
        new_position = random.randint(0, N_TILES * N_TILES - 1)
        while new_position in self.__occ_tiles:
            new_position = random.randint(0, N_TILES * N_TILES - 1)
        self.__occ_tiles.add(new_position)

        self.__children_field.importMFNodeFromString(-1, 'DEF DUCK' + str(
            self.__duck_count) + ' RubberDuck {translation ' +
            str(self.get_x_coordinate_from_tile_number(new_position)) + ' ' +
            str(self.get_y_coordinate_from_tile_number(new_position)) + ' 0 scale 0.5}')
        self.__duck_tiles[self.__duck_count] = new_position
        self.__duck_time_left[self.__duck_count] = LIFE_SPAN
        self.__duck_refs[self.__duck_count] = self.__robot.getFromDef(
            'DUCK' + str(self.__duck_count))

        # push belief that there is a new duck which will trigger
        # the reactive rule to add a new desire to retireve it
        belief = Belief()
        belief.name = 'at_gar'
        belief.pddl_type = 2
        belief.params = ['g' + str(self.__duck_count), 't' + str(new_position)]
        self.new_belief_publisher.publish(belief)

        belief.name = 'to_recycle'
        belief.pddl_type = 2
        belief.params = ['g' + str(self.__duck_count)]
        self.new_belief_publisher.publish(belief)

        self.__node.get_logger().info('g%d spawned at t%d' %(self.__duck_count, new_position))

        self.__duck_count += 1

    def remove_elapsed_ducks(self):
        i = 0
        while self.__duck_time_left[i] is not None:
            if self.__duck_time_left[i] == 0 and self.__duck_catched[i] == False:
                self.__duck_refs[i].remove()
                self.__node.get_logger().info('g%d timed out!' %(i))

                belief = Belief()

                belief.name = 'to_recycle'
                belief.pddl_type = 2
                belief.params = ['g' + str(i)]
                self.delete_belief_publisher.publish(belief)

                belief.name = 'deleted'
                belief.pddl_type = 2
                belief.params = ['g' + str(i)]
                self.new_belief_publisher.publish(belief)

                belief.name = 'free'
                belief.pddl_type = 2
                belief.params = ['e_puck']
                self.new_belief_publisher.publish(belief)

                belief.name = 'holding'
                belief.pddl_type = 2
                belief.params = ['e_puck', 'g' + str(i)]
                self.delete_belief_publisher.publish(belief)

            self.__duck_time_left[i] -= 1
            i += 1

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
        self.__node.get_logger().info('g%d removed.' % (msg.data))
        if self.__first_duck_done == False:
            self.__duck_refs[0].getField(
                'translation').setSFVec3f([20, 20, 20])
            self.__duck_tiles[0] = -1
        else:
            self.__duck_refs[msg.data].remove()
        
        #self.__occ_tiles.remove(self.__duck_tiles[msg.data])
        self.__duck_catched[msg.data] = True    

    def putdown_garbage_callback(self, msg):
        if self.__first_duck_done == False:
            self.__first_duck_done = True
            self.__duck_refs[0].getField(
                'translation').setSFVec3f([-0.496798, 0.97926, 0])
        
        #delete belief that the garbage needs to be recycled
        belief = Belief()
        belief.name = 'to_recycle'
        belief.pddl_type = 2
        belief.params = ['g' + str(msg.data)]
        self.delete_belief_publisher.publish(belief)

    def move_callback(self, msg):
        self.__robot_position = msg.data

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
