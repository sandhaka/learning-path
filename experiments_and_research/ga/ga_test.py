import random

import pytest

from .gene import Gene
from .operations import main, crossover, mutation

""" gene tests """


def test_gene():
    gene = Gene([True, False, True], None)
    assert gene.value == [True, False, True]
    assert gene.fitness is None
    print(gene)


def test_gene_equality():
    gene1 = Gene([True, False, True], None)
    gene2 = Gene([True, False, True], None)
    assert gene1 == gene2
    assert gene1 is not gene2


def test_gene_greater_than():
    gene1 = Gene([True, False, True], 0.56)
    gene2 = Gene([True, False, True], 0.78)
    assert gene2 > gene1
    assert gene2 >= gene1
    assert gene1 < gene2
    assert gene1 <= gene2


def test_gene_ctor_error():
    try:
        Gene([], None)
        assert False
    except AssertionError:
        assert True


""" comprehensive test """


@pytest.mark.skip("This test takes a long time to run")
def test_ga_string_target():
    target = "hello world"
    target_value = [c for c in target]

    def seed_method(x):
        return [random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in x]

    generated, generation = main(
        target_value=target_value,
        custom_evaluate_fitness=None,
        seed_method="custom",
        gene_seed=seed_method,
        max_generations=5000,
    )
    assert generated == Gene(target_value)
    assert generation > 0
