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

    online_bdi_spazza_share_dir = get_package_share_directory('online_bdi_spazza')

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

    # # get static map info status sensor 
    # load_map_sensor = AgentSensor(
    #     package='online_bdi_spazza',
    #     executable='load_map_sensor',
    #     name=ROBOT_NAME+'_load_map',
    #     specific_params=[
    #         {"init_sleep": 2},
    #         {"sensing_freq": 1.0}
    #     ])

    # # get dynamic map info in a restricted grid 
    # agent_area_sensor = AgentSensor(
    #     package='online_bdi_spazza',
    #     executable='agent_area_sensor',
    #     name=ROBOT_NAME+'_area_sensor',
    #     specific_params=[
    #         {"init_sleep": 4},
    #         {"sensing_freq": 1.0},
    #         {"detection_depth": 3},
    #         {"should_patrol": True}
    #     ])

    pmode = 'online'
    reschedule_policy = 'NO_PREEMPT'
    if pmode == 'online':
        reschedule_policy = 'CLEAN_PREEMPT'

    plastic_agent_ld = AgentLaunchDescription(
        agent_id=ROBOT_NAME,
        agent_group=ROBOT_GROUP_NAME,
        init_params={
            'pddl_file': os.path.join(online_bdi_spazza_share_dir, 'pddl', 'e_puck', 'spazza-domain.pddl'),
            'init_bset': os.path.join(online_bdi_spazza_share_dir, 'launch', 'init_e_puck', 'init_bset.yaml'),
            'init_dset': os.path.join(online_bdi_spazza_share_dir, 'launch', 'init_e_puck', 'init_dset.yaml'),
            'init_reactive_rules_set': os.path.join(online_bdi_spazza_share_dir, 'launch', 'init_e_puck', 'init_rrules.yaml'.format(pmode)),
            'planner': 'JAVAFF',
            'comp_plan_tries': 4,
            'exec_plan_tries': 4,
            'planning_mode':pmode,
            'reschedule_policy': reschedule_policy,
            'search_interval': 400,
            # 'max_pplan_size': 32,
            'min_commit_steps': 1,
            #'sim_to_n': 3,
            'max_null_search_intervals': 16,
            'debug_log_active': ['javaff', 'scheduler', 'event_listener']
        },
        actions=[action_move, action_pickup, action_putdown],
        run_only_psys2=False
    ) 

    return plastic_agent_ld