#include <iostream>
#include <string>
#include <random>
#include <ctime>

using namespace std;

int main() {
	unsigned seed = static_cast<unsigned>(time(nullptr));
	mt19937 gen(seed);
	uniform_int_distribution<int> dist(0, 1);

	string sequence;

	for (int i = 0; i < 128; ++i) {
		sequence += dist(gen) ? '1' : '0';
		
	}

	cout << sequence;

	return 0;
}