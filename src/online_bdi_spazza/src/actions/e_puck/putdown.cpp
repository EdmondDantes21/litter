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
            publisher_->publish(get_garbage_index());
            progress = 0.0;
        }
        return 0.25f;
    }

    std_msgs::msg::Int16 get_garbage_index()
    {
        // arguments will be of the following form:
        //[0]: "e_puck", [1]: "t1", [2]: "b",  [3]: "g2"
        std::vector<std::string> arguments = this->getArguments();
        int garbageIndex = arguments[3][1] - '0';
        if (arguments[3][2] >= '0' && arguments[3][2] <= '9')
            garbageIndex = garbageIndex * 10 + (arguments[3][2] - '0');

        RCLCPP_INFO(this->get_logger(), "putting down g%d", garbageIndex);

        auto msg = std_msgs::msg::Int16();
        msg.data = garbageIndex;
        return msg;
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
