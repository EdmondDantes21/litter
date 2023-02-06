#include <iostream>
#include <fstream>

std::ofstream file("tmp.yaml", std::ofstream::out | std::ofstream::trunc);

int main(int argc, char **argv)
{
    int N = (argc < 2) ? 100 : std::stoi(argv[1]);

    for (int i = 0; i < N; i++) {
        file << "- condition:\n";
        file << "    clauses:\n";
        file << "      - literals:\n";
        file << "          - check: \"EX\"\n";
        file << "            condition_to_check:\n";
        file << "              name: \"g" << std::to_string(i) << "\"\n";
        file << "              pddl_type: 1\n";
        file << "              type: \"garbage\"\n\n";
        file << "          - check: \"T\"\n";
        file << "            condition_to_check:\n";
        file << "              name: \"to_recycle\"\n";
        file << "              pddl_type: 2\n";
        file << "              params:\n";
        file << "                - \"g" << std::to_string(i) << "\"\n\n";
        file << "          - check: \"F\"\n";
        file << "            condition_to_check:\n";
        file << "              name: \"deleted\"\n";
        file << "              pddl_type: 2\n";
        file << "              params:\n";
        file << "                - \"g" << std::to_string(i) << "\"\n\n";

        file << "  reactive_rules:\n";
        file << "    - set: desire\n";
        file << "      operation: ADD\n";
        file << "      value:\n";
        file << "        name: \"throw_new_garbage_" << std::to_string(i) << "\"\n";
        file << "        priority: 0.6\n";
        file << "        deadline: 1000\n";
        file << "        value:\n";
        file << "          - name: \"at_gar\"\n";
        file << "            pddl_type: 2\n";
        file << "            params:\n";
        file << "              - \"g" << std::to_string(i) << "\"\n";
        file << "              - \"t1\"\n\n";
        
        file << "- condition:\n";
        file << "    clauses:\n";
        file << "      - literals:\n";
        file << "        - check: \"T\"\n";
        file << "          condition_to_check:\n";
        file << "            name: \"deleted\"\n";
        file << "            pddl_type: 2\n";
        file << "            params:\n";
        file << "              - \"g" << std::to_string(i) << "\"\n\n";

        file << "  reactive_rules:\n";
        file << "    - set: desire\n";
        file << "      operation: DEL\n";
        file << "      value:\n";
        file << "        name: \"throw_new_garbage_" << std::to_string(i) << "\"\n";
        file << "        priority: 0.6\n";
        file << "        deadline: 1000\n";
        file << "        value:\n";
        file << "          - name: \"at_gar\"\n";
        file << "            pddl_type: 2\n";
        file << "            params:\n";
        file << "              - \"g" << std::to_string(i) << "\"\n";
        file << "              - \"t1\"\n";
    }

    return 0;    
}