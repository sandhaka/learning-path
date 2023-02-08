from .gene import Gene


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
