import sys
from ament_index_python.packages import get_package_share_directory

ros2_bdi_bringup_dir = get_package_share_directory('ros2_bdi_bringup')
sys.path.append(ros2_bdi_bringup_dir + '/launch/')
from bdi_agent import AgentLaunchDescription
from bdi_agent import AgentAction

def generate_launch_description():
    
    ROBOT_NAME = "e_puck"
    ROBOT_GROUP_NAME = "robots"

    bdi_tests_share_dir = get_package_share_directory('bdi_spazza')

    # perform moving toward
    action_move = AgentAction(
        package='bdi_spazza',
        executable='move',
        name='move'
    )

    # perform sweeping action
    action_pickup = AgentAction(
        package='bdi_spazza',
        executable='pickup',
        name='pickup'
    )
    
    # recharging action
    action_putdown = AgentAction(
        package='bdi_spazza',
        executable='putdown',
        name='putdown'
    )

    ld = AgentLaunchDescription(
        agent_id=ROBOT_NAME,
        agent_group=ROBOT_GROUP_NAME,
        init_params={
            'pddl_file': bdi_tests_share_dir + '/pddl/spazza_domain.pddl',
            'init_bset': bdi_tests_share_dir + '/launch/init/init_bset.yaml',
            'init_dset': bdi_tests_share_dir + '/launch/init/init_dset.yaml',
            'belief_ck': [ROBOT_GROUP_NAME],   
            'belief_w':  [ROBOT_GROUP_NAME],   
            'desire_ck': [ROBOT_GROUP_NAME],   
            'desire_w':  [ROBOT_GROUP_NAME],   
            'desire_pr': [0.6, 0.95],
            'comp_plan_tries': 16,
            'exec_plan_tries': 4,
            'debug_log_active': ['belief_manager', 'scheduler', 'plan_director']
        },
        actions=[action_move, action_pickup, action_putdown],
        run_only_psys2=False
    ) 

    return ld