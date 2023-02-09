import random
import typing

from .gene import Gene

""" Operations on genes """


def crossover(gene1: Gene, gene2: Gene):
    assert len(gene1.value) == len(gene2.value)
    slice_index = random.randint(0, len(gene1.value) - 1)
    child_1 = Gene(gene1.value[:slice_index] + gene2.value[slice_index:])
    child_2 = Gene(gene2.value[:slice_index] + gene1.value[slice_index:])
    return child_1, child_2


def mutation(child: Gene, mutation_rate: float, possible_values: list[typing.Any]):
    if random.uniform(0, 1) < mutation_rate:
        mutation_pos = random.randint(0, len(possible_values) - 1)
        child.value[mutation_pos] = possible_values[mutation_pos]


def evaluate_fitness(gene_value: list[bool], target_value: list[bool]):
    assert len(gene_value) == len(target_value)
    fitness = 0
    for i in range(len(target_value)):
        if gene_value[i] == target_value[i]:
            fitness += 1
    return fitness / len(target_value)


""" Main """


def main(
    target_value: list[typing.Any],
    custom_evaluate_fitness: callable = None,
    seed_method="random_default",
    gene_seed=None,
    max_generations=1000,
    population_size=200,
    selection=30,
    mutation_rate=0.4,
):
    assert population_size > 0
    assert selection < population_size
    assert 0 < mutation_rate < 1
    assert max_generations > 0
    evaluate = evaluate_fitness
    if custom_evaluate_fitness is not None:
        evaluate = custom_evaluate_fitness

    # Setup
    population = []
    domain_values = list(set(target_value))
    if seed_method == "random_default":
        for _ in range(population_size):
            population.append(Gene([random.choice([0, 1]) for _ in target_value]))
    elif seed_method == "custom":
        assert gene_seed is not None
        for _ in range(population_size):
            population.append(Gene(gene_seed(target_value)))
    if len(population) == 0:
        raise ValueError("Invalid seed method")

    # Population validation
    for i in target_value:
        i_found = False
        for gene in population:
            if i in gene.value:
                i_found = True
                break
        if not i_found:
            raise ValueError("Invalid seed")

    # Main loop
    for generation in range(max_generations + 1):
        for gene in population:
            gene.fitness = evaluate(gene.value, target_value)

        # Sort by fitness
        population.sort(reverse=True)

        if population[0].fitness == 1 or generation == max_generations:
            return population[0], generation

        population = population[:selection]

        for _ in range(population_size - selection):
            parent_1 = population[random.randint(0, selection - 1)]
            parent_2 = population[random.randint(0, selection - 1)]
            child_1, child_2 = crossover(parent_1, parent_2)
            mutation(child_1, mutation_rate, domain_values)
            mutation(child_2, mutation_rate, domain_values)
            population.extend([child_1, child_2])
