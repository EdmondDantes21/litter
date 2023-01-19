#include <iostream>
using namespace std;

#define N_TILES 7

int main() {
	for (int i = 0; i < 49; i++) {
		int x = i / N_TILES;
        int y = i % N_TILES;

        //up down left right
		if (x + 1 < N_TILES)
			cout << "(adjacent t" << i << " t" << i + N_TILES << ")\n";
		if (x - 1 >= 0)
			cout << "(adjacent t" << i << " t" << i - N_TILES << ")\n";
        if (y + 1 < N_TILES)
            cout << "(adjacent t" << i << " t" << i + 1 << ")\n";
        if (y - 1 >= 0)
            cout << "(adjacent t" << i << " t" << i - 1 << ")\n";

        //diagonals
        if (x + 1 < N_TILES && y - 1 >= 0)
            cout << "(adjacent t" << i << " t" << i + N_TILES - 1 << ")\n";
        if (x + 1 < N_TILES && y + 1 < N_TILES)
            cout << "(adjacent t" << i << " t" << i + N_TILES + 1 << ")\n";
        if (x - 1 >= 0 && y - 1 >= 0)
            cout << "(adjacent t" << i << " t" << i - N_TILES - 1 << ")\n";
        if (x - 1 >= 0 && y + 1 < N_TILES)
            cout << "(adjacent t" << i << " t" << i - N_TILES + 1 << ")\n";
	}
    return 0;
}