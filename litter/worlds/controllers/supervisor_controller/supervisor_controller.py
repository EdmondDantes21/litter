from controller import Supervisor

TIME_STEP = 32

robot = Supervisor()  # create Supervisor instance

bottle_node = robot.getFromDef('BEER_BOTTLE')
translation_field = bottle_node.getField('translation')

i = 0
while robot.step(TIME_STEP) != -1:
    if (i == 0):
        new_value = [0.5, 0, 0]
        translation_field.setSFVec3f(new_value)
        i += 1