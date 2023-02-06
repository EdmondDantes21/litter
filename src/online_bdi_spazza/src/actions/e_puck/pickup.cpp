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
        publisher_ = this->create_publisher<std_msgs::msg::Int16>("pickup", 4);
        publisher_->on_activate();
    }

    float advanceWork()
    {
        if (state == 0)
            publisher_->publish(get_garbage_index());

        state = state == 3 ? 0 : state + 1;
        return 0.25f;
    }

    std_msgs::msg::Int16 get_garbage_index()
    {
        // arguments will be of the following form:
        //[0]: "e_puck", [1]: "t1", [2]: "g2"
        std::vector<std::string> arguments = this->getArguments();
        int garbageIndex = arguments[2][1] - '0';
        if (arguments[2][2] >= '0' && arguments[2][2] <= '9')
            garbageIndex = garbageIndex * 10 + (arguments[2][2] - '0');

        RCLCPP_INFO(this->get_logger(), "picking up duck nr. %d", garbageIndex);

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
    short int state = 0;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto actionNode = std::make_shared<Pickup>();
    rclcpp::spin(actionNode->get_node_base_interface());

    rclcpp::shutdown();

    return 0;
}
