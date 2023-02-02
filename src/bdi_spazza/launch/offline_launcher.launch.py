import sys
from ament_index_python.packages import get_package_share_directory

ros2_bdi_bringup_dir = get_package_share_directory('ros2_bdi_bringup')
sys.path.append(ros2_bdi_bringup_dir + '/launch/')
from bdi_agent import AgentAction
from bdi_agent import AgentLaunchDescription

def generate_launch_description():

    ROBOT_NAME = "e_puck"
    ROBOT_GROUP_NAME = "robots"

    bdi_spazza_share_dir = get_package_share_directory('bdi_spazza')

    action_move = AgentAction(
        package='bdi_spazza',
        executable='move',
        name='move'
    )

    action_pickup = AgentAction(
        package='bdi_spazza',
        executable='pickup',
        name='pickup'
    )

    action_putdown = AgentAction(
        package='bdi_spazza',
        executable='putdown',
        name='putdown'
    )

    ld = AgentLaunchDescription(
        agent_id=ROBOT_NAME,
        agent_group=ROBOT_GROUP_NAME,
        init_params={
            'pddl_file': bdi_spazza_share_dir + '/pddl/e_puck/spazza-domain.pddl',
            'init_bset': bdi_spazza_share_dir + '/launch/init_e_puck/init_bset.yaml',
            #'init_dset': bdi_spazza_share_dir + '/launch/init_e_puck/init_dset.yaml',
            'init_reactive_rules_set': bdi_spazza_share_dir + '/launch/init_e_puck/spawn_rrules.yaml',
            'belief_ck': [ROBOT_GROUP_NAME],
            'belief_w':  [ROBOT_GROUP_NAME],
            'desire_ck': [ROBOT_GROUP_NAME],
            'desire_w':  [ROBOT_GROUP_NAME],
            'desire_pr': [0.99],
            'comp_plan_tries': 16,
            'exec_plan_tries': 4,
            'reschedule_policy': 'NO_PREEMPT',
            'debug_log_active': ['belief_manager', 'scheduler', 'plan_director']
        },
        actions=[action_move, action_pickup, action_putdown],
        run_only_psys2=False
    )

    return ld
