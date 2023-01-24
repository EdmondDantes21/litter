#include "ros2_bdi_skills/bdi_action_executor.hpp"
#include "rclcpp/rclcpp.hpp"

class PutDown : public BDIActionExecutor
{
    public:
        PutDown()
        : BDIActionExecutor("putdown", 4)
        {}

        float advanceWork()
        {
            RCLCPP_INFO(this->get_logger(), "putting down...\n");
            return 0.0625f;            
        }

    private:
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  
  auto actionNode = std::make_shared<PutDown>();
  rclcpp::spin(actionNode->get_node_base_interface());

  rclcpp::shutdown();

  return 0;
}
