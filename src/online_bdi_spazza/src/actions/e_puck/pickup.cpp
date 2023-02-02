#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_lifecycle/lifecycle_node.hpp"

#include "std_msgs/msg/int16.hpp"

class Pickup : public BDIActionExecutor
{
public:
    Pickup()
        : BDIActionExecutor("pickup", 1)
    {
    }

    float advanceWork()
    {
        RCLCPP_INFO(this->get_logger(), "picking up...");
        return 0.025f;
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto actionNode = std::make_shared<Pickup>();
    rclcpp::spin(actionNode->get_node_base_interface());

    rclcpp::shutdown();

    return 0;
}
