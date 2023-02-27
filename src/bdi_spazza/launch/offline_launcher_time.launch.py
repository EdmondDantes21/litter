import sys
import os
import os.path

from ament_index_python.packages import get_package_share_directory

ros2_bdi_bringup_dir = get_package_share_directory('ros2_bdi_bringup')
sys.path.append(ros2_bdi_bringup_dir + '/launch/')
from bdi_agent import AgentLaunchDescription
from bdi_agent_skills import AgentAction
from bdi_agent_skills import AgentSensor

def generate_launch_description():
    ROBOT_NAME = 'e_puck'
    ROBOT_GROUP_NAME = 'robots'

    bdi_spazza_share_dir = get_package_share_directory('online_bdi_spazza')

    #move action
    action_move = AgentAction(
        package='online_bdi_spazza',
        executable='move',
        name='move',
        specific_params=[]
    )
    
    #pickup action
    action_pickup = AgentAction(
        package='online_bdi_spazza',
        executable='pickup',
        name='pickup',
        specific_params=[]
    )

    #putdown action
    action_putdown = AgentAction(
        package='online_bdi_spazza',
        executable='putdown',
        name='putdown',
        specific_params=[]
    )

    ld = AgentLaunchDescription(
        agent_id=ROBOT_NAME,
        agent_group=ROBOT_GROUP_NAME,
        init_params={
            'pddl_file': bdi_spazza_share_dir + '/pddl/e_puck/spazza-domain-time.pddl',
            'init_bset': bdi_spazza_share_dir + '/launch/init_e_puck/init_bset_time.yaml',
            #'init_dset': bdi_spazza_share_dir + '/launch/init_e_puck/init_dset.yaml',
            'init_reactive_rules_set': bdi_spazza_share_dir + '/launch/init_e_puck/init_rrules_time.yaml',
            'belief_ck': [ROBOT_GROUP_NAME],
            'belief_w':  [ROBOT_GROUP_NAME],
            'desire_ck': [ROBOT_GROUP_NAME],
            'desire_w':  [ROBOT_GROUP_NAME],
            'desire_pr': [0.99],
            'comp_plan_tries': 4    ,
            'exec_plan_tries': 4,
            'reschedule_policy': 'NO_PREEMPT',
            'debug_log_active': ['belief_manager', 'scheduler', 'plan_director']
        },
        actions=[action_move, action_pickup, action_putdown],
        run_only_psys2=False
    )

    return ld