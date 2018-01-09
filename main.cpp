#include <iostream>
#include "src/World.h"
#include "src/Common.h"
#include <chrono>

using namespace std;

int main(int argc, char* argv[]) {
    auto t1 = std::chrono::high_resolution_clock::now();

    printf("Init binding matrix\n");
    Common::init_binding_matrix(897685687);

    auto t2 = std::chrono::high_resolution_clock::now();
    auto duration_binding = std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count();
    printf("Done in %li ms\n", duration_binding);

    auto t3 = std::chrono::high_resolution_clock::now();
    printf("Create World\n");

	int dim = 32;
	if (argc > 1) {
	  dim = atoi(argv[1]);
	}

    World* world = new World(dim, dim, 897986875);
    auto t4 = std::chrono::high_resolution_clock::now();
    auto duration_hw = std::chrono::duration_cast<std::chrono::milliseconds>(t4-t3).count();
    printf("Done in %li ms\n", duration_hw);

    auto t5 = std::chrono::high_resolution_clock::now();
    printf("Initialize environment\n");
    world->init_environment();
    auto t6 = std::chrono::high_resolution_clock::now();
    auto duration_env = std::chrono::duration_cast<std::chrono::milliseconds>(t6-t5).count();
    printf("Done in %li ms\n", duration_env);

    bool test = false;

    printf("Initialize random population\n");
    auto t7 = std::chrono::high_resolution_clock::now();
    world->random_population();
    auto t8 = std::chrono::high_resolution_clock::now();
    auto duration_pop = std::chrono::duration_cast<std::chrono::milliseconds>(t8 - t7).count();
    printf("Done in %li ms\n", duration_pop);
    printf("Run evolution\n");
    auto t9 = std::chrono::high_resolution_clock::now();
    world->run_evolution();
    auto t11 = std::chrono::high_resolution_clock::now();
    auto duration_evo = std::chrono::duration_cast<std::chrono::milliseconds>(t11 - t9).count();
    printf("Done in %li ms\n", duration_evo);

    auto t10 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t10-t1).count();
    printf("Total time : %li ms\n", duration);
}
