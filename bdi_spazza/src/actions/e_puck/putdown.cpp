#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_lifecycle/lifecycle_node.hpp"

#include "std_msgs/msg/int16.hpp"

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
        auto msg = std_msgs::msg::Int16();
        msg.data = 1;
        publisher_->publish(msg);
        return 0.25f;
    }

private:
    std::shared_ptr<rclcpp_lifecycle::LifecyclePublisher<std_msgs::msg::Int16>> publisher_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto actionNode = std::make_shared<PutDown>();
    rclcpp::spin(actionNode->get_node_base_interface());

    rclcpp::shutdown();

    return 0;
}
