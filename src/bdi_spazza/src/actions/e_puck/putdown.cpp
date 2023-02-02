#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_lifecycle/lifecycle_node.hpp"

#include "std_msgs/msg/int16.hpp"
#include "ros2_bdi_interfaces/msg/desire.hpp"

using Desire = ros2_bdi_interfaces::msg::Desire;

class PutDown : public BDIActionExecutor
{
public:
    PutDown()
        : BDIActionExecutor("putdown", 1)
    {
        publisher_ = this->create_publisher<std_msgs::msg::Int16>("putdown", 4);
        publisher_->on_activate();
    }

    float advanceWork()
    {   
        progress += 0.25;   
        if (progress == 1.0) {
            auto msg = std_msgs::msg::Int16();
            msg.data = 1;
            publisher_->publish(msg);
            progress = 0.0;
        }
        return 0.25f;
    }

    rclcpp_lifecycle::node_interfaces::LifecycleNodeInterface::CallbackReturn
    on_activate(const rclcpp_lifecycle::State &previous_state)
    {
        return BDIActionExecutor::on_activate(previous_state);
    }

    rclcpp_lifecycle::node_interfaces::LifecycleNodeInterface::CallbackReturn
    on_deactivate(const rclcpp_lifecycle::State &previous_state)
    {
        return BDIActionExecutor::on_deactivate(previous_state);
    }

private:
    std::shared_ptr<rclcpp_lifecycle::LifecyclePublisher<std_msgs::msg::Int16>> publisher_;
    float progress = 0.0;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto actionNode = std::make_shared<PutDown>();
    rclcpp::spin(actionNode->get_node_base_interface());

    rclcpp::shutdown();

    return 0;
}
