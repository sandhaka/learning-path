class Gene:
    def __init__(self, value: list[bool], fitness):
        assert value is not None and len(value) > 0
        self.value = value
        self.fitness = fitness

    def __repr__(self):
        return "Gene(value={}, fitness={})".format(self.value, self.fitness)

    def __str__(self):
        return "Gene(value={}, fitness={})".format(self.value, self.fitness)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __ne__(self, other):
        return self.value != other.value
