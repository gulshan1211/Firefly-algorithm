import numpy as np
import random


def firefly_algorithm(adj_matrix, population_size, max_generations, alpha, beta, gamma):
    num_vertices = len(adj_matrix)

    # Generate initial population using nearest insertion heuristic
    population = []
    for _ in range(population_size):
        solution = nearest_insertion_heuristic(adj_matrix)
        population.append(solution)

    # Evaluate fitness of each firefly
    fitness = [evaluate_fitness(solution, adj_matrix) for solution in population]

    for generation in range(max_generations):
        # Update fireflies
        for i in range(population_size):
            for j in range(population_size):
                if fitness[i] > fitness[j]:
                    attractiveness = beta * np.exp(-gamma * calculate_distance(population[i], population[j]))
                    for k in range(num_vertices):
                        population[i][k] += int(round(attractiveness * (population[j][k] - population[i][k])))
                    fitness[i] = evaluate_fitness(population[i], adj_matrix)

        # Sort population by fitness in ascending order
        sorted_indices = sorted(range(len(fitness)), key=lambda k: fitness[k])
        population = [population[i] for i in sorted_indices]
        fitness = [fitness[i] for i in sorted_indices]

        # Perform local search using best improvement technique
        for i in range(population_size):
            population[i] = best_improvement(population[i], adj_matrix)
            fitness[i] = evaluate_fitness(population[i], adj_matrix)

        best_solution = population[0]
        best_fitness = fitness[0]

        print("Generation:", generation, "Best Fitness:", best_fitness)

    return best_solution, best_fitness


def nearest_insertion_heuristic(adj_matrix):
    num_vertices = len(adj_matrix)
    unvisited = set(range(1, num_vertices))

    # Start from a random vertex
    start_vertex = random.randint(0, num_vertices - 1)
    unvisited.remove(start_vertex)
    solution = [start_vertex]

    while unvisited:
        current_vertex = solution[-1]
        nearest_neighbor = min(unvisited, key=lambda v: adj_matrix[current_vertex][v])
        insertion_index, _ = min(((i, adj_matrix[solution[i]][nearest_neighbor] + adj_matrix[nearest_neighbor][
            solution[i + 1]] - adj_matrix[solution[i]][solution[i + 1]])) for i in range(len(solution) - 1))
        solution.insert(insertion_index + 1, nearest_neighbor)
        unvisited.remove(nearest_neighbor)

    return solution

# Rest of the code remains unchanged
