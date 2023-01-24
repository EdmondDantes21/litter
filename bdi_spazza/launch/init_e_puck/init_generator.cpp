#include <iostream>
#include <fstream>
using namespace std;

#define N_TILES 7

ofstream file("tmp.txt");

void printAdjacent(int, int);

int main() {
	for (int i = 0; i < 49; i++) {
        //generate tile declaration
		/*cout << "- name: \"t" << i << "\"\n";
        cout << "  pddl-type: 1\n";
        cout << "  type: \"tile\"\n"; */
        
        //generate walkable predicates
        /*cout << "- name: \"walkable\"\n";
        cout << "  pddl-type: 2\n";
        cout << "  params: \n";
        cout << "    - \"t" << i << "\"\n";*/

        //generate adjacent declaration
		int x = i / N_TILES;
        int y = i % N_TILES;

        //up down left right
		if (x + 1 < N_TILES)
            printAdjacent(i, i + N_TILES);
		if (x - 1 >= 0)
            printAdjacent(i, i - N_TILES);
        if (y + 1 < N_TILES)
            printAdjacent(i, i + 1);
        if (y - 1 >= 0)
            printAdjacent(i, i - 1);

        //diagonals
        if (x + 1 < N_TILES && y - 1 >= 0)
            printAdjacent(i, i + N_TILES - 1);
        if (x + 1 < N_TILES && y + 1 < N_TILES)
            printAdjacent(i, i + N_TILES + 1);
        if (x - 1 >= 0 && y - 1 >= 0)
            printAdjacent(i, i - N_TILES - 1);
        if (x - 1 >= 0 && y + 1 < N_TILES)
            printAdjacent(i, i - N_TILES + 1);
    }
    file.close();
    return 0;
}

void printAdjacent(int a, int b) {
    file << "- name: \"adjacent\"\n";
    file << "  pddl-type: 2\n";
    file << "  params: \n";
    file << "    - \"t" << a << "\"\n";
    file << "    - \"t" << b << "\"\n";
}