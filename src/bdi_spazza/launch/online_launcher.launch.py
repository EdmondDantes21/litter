import sys
import os
import os.path
from ament_index_python.packages import get_package_share_directory

ros2_bdi_bringup_dir = get_package_share_directory('ros2_bdi_bringup')
sys.path.append(ros2_bdi_bringup_dir + '/launch/')
from bdi_agent import AgentAction
from bdi_agent import AgentLaunchDescription

def generate_launch_description():

    ROBOT_NAME = "e_puck"
    ROBOT_GROUP_NAME = "robots"

    bdi_spazza_share_dir = get_package_share_directory('bdi_spazza')

    # perform moving toward
    action_move = AgentAction(
        package='bdi_spazza',
        executable='move',
        name='move',
        specific_params=[]
    )

    # perform sweeping action
    action_pickup = AgentAction(
        package='bdi_spazza',
        executable='pickup',
        name='pickup',
        specific_params=[]
    )

    # recharging action
    action_putdown = AgentAction(
        package='bdi_spazza',
        executable='putdown',
        name='putdown',
        specific_params=[]
    )

    pmode = 'online'
    reschedule_policy = 'NO_PREEMPT'
    if pmode == 'online':
        reschedule_policy = 'CLEAN_PREEMPT'

    ld = AgentLaunchDescription(
        agent_id=ROBOT_NAME,
        agent_group=ROBOT_GROUP_NAME,
        init_params={
            'pddl_file': os.path.join(bdi_spazza_share_dir, 'pddl', 'e_puck', 'spazza-domain.pddl'),
            'init_bset': os.path.join(bdi_spazza_share_dir, 'launch', 'init_e_puck', 'init_e_puck_bset.yaml'),
            #'init_dset': bdi_spazza_share_dir + '/launch/init_e_puck/init_e_puck_dset.yaml',
            'init_reactive_rules_set': os.path.join(bdi_spazza_share_dir, 'launch', 'init_e_puck', 'online', 'init_e_puck_rrules.yaml'.format(pmode)),
            'planner': 'JAVAFF',
            'comp_plan_tries': 4,
            'exec_plan_tries': 4,
            'planning_mode':pmode,
            'reschedule_policy': reschedule_policy,
            'search_interval': 400,
            'min_commit_steps': 1,
            'max_null_search_intervals': 16,
            'debug_log_active': ['javaff', 'scheduler', 'event_listener']
        },
        actions=[action_move, action_pickup, action_putdown],
        run_only_psys2=False
    )

    return ld
