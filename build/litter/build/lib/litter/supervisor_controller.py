import rclpy

TIME_STEP = 32

class RobotSupervisor:
    i = 0
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        if not rclpy.ok():
            rclpy.init(args=None)

        self.__node = rclpy.create_node(self.__robot.getName()+'_driver')

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        if (self.i == 0):
            bottle_node = self.__robot.getFromDef('BEER_BOTTLE')
            translation_field = bottle_node.getField('translation')
            new_value = [2.5, 0, 0]
            translation_field.setSFVec3f(new_value)
            i += 1

    