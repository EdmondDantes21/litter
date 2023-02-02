#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_lifecycle/lifecycle_node.hpp"

#include "std_msgs/msg/int16.hpp"
#include "std_msgs/msg/empty.hpp"

using std::placeholders::_1;

class Move : public BDIActionExecutor
{
public:
    Move()
        : BDIActionExecutor("move", 1)
    {
        publisher_ = this->create_publisher<std_msgs::msg::Int16>("move", 10);

        subscriber_ = this->create_subscription<std_msgs::msg::Empty>(
            "move_completed", 4,
            std::bind(&Move::move_completed_callback, this, _1));

        publisher_->on_activate(); // activate publisher when using LifeCycle node
    }

    float advanceWork()
    {
        // arguments will be of the following form:
        //[0]: "e_puck", [1]: "t1", [2]: "t0"
        std::vector<std::string> arguments = this->getArguments();

        // telling webots ros2 topic to move the e_puck

        auto msg = std_msgs::msg::Int16();
        msg.data = arguments[2][1] - '0'; // -'0' trick to convert char to int
        if (arguments[2][2] >= '0' && arguments[2][2] <= '9')
            msg.data = (arguments[2][1] - '0') * 10 + (arguments[2][2] - '0');
        publisher_->publish(msg);

        if (move_completed)
        {
            move_completed = false;
            return 1.0f;
        }

        return 0.025f;
    }

    void move_completed_callback(const std_msgs::msg::Empty::SharedPtr msg)
    {
        move_completed = true;
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
    rclcpp::Subscription<std_msgs::msg::Empty>::SharedPtr subscriber_;
    bool move_completed = false;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto actionNode = std::make_shared<Move>();
    rclcpp::spin(actionNode->get_node_base_interface());

    rclcpp::shutdown();

    return 0;
}
