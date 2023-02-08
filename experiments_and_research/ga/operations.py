import random
from .gene import Gene


def crossover(gene1: Gene, gene2: Gene):
    assert len(gene1.value) == len(gene2.value)
    slice_index = random.randint(0, len(gene1.value) - 1)
    child_1 = Gene(gene1.value[:slice_index] + gene2.value[slice_index:], None)
    child_2 = Gene(gene2.value[:slice_index] + gene1.value[slice_index:], None)
    return child_1, child_2


def mutation(child: Gene, mutation_rate: float):
    if random.uniform(0, 1) < mutation_rate:
        mutation_pos = random.randint(0, len(child.value) - 1)
        child.value[mutation_pos] = not child.value[mutation_pos]
