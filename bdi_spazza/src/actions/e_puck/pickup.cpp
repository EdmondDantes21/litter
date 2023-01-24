#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"

class Pickup : public BDIActionExecutor
{
    public:
        Pickup()
        : BDIActionExecutor("pickup", 4)
        {}

        float advanceWork()
        {
            RCLCPP_INFO(this->get_logger(), "picking up...\n");
            return 0.0625f;            
        }

    private:
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  
  auto actionNode = std::make_shared<Pickup>();
  rclcpp::spin(actionNode->get_node_base_interface());

  rclcpp::shutdown();

  return 0;
}
