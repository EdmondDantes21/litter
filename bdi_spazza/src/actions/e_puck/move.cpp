#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"

class Move : public BDIActionExecutor
{
    public:
        Move()
        : BDIActionExecutor("move", 4)
        {}

        float advanceWork()
        {
            RCLCPP_INFO(this->get_logger(), "moving...\n");
            return 0.0625f;            
        }

    private:
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  
  auto actionNode = std::make_shared<Move>();
  rclcpp::spin(actionNode->get_node_base_interface());

  rclcpp::shutdown();

  return 0;
}
