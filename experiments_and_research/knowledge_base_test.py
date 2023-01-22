from functools import reduce
from itertools import product


def a(sym):
    return Atom(sym)


def dissociate(op, clause):
    results = []

    def collect(clause):
        if isinstance(clause, op):
            collect(clause.lchild)
            collect(clause.rchild)
        else:
            results.append(clause)

    if isinstance(clause, Atom):
        return [clause]
    if isinstance(clause, Not):
        return [clause]
    collect(clause)
    return results


class Formula:
    def __invert__(self):
        return Not(self)

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __rshift__(self, other):
        return Implies(self, other)

    def __lshift__(self, other):
        return Iff(self, other)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.eq(other)

    def v(self, v):
        raise NotImplementedError("Plain formula can not be valuated")

    def _t(self, left, right):
        while True:
            found = True
            for item in left:
                if item in right:
                    return None
                if not isinstance(item, Atom):
                    left.remove(item)
                    tup = item._tleft(left, right)
                    left, right = tup[0]
                    if len(tup) > 1:
                        v = self._t(*tup[1])
                        if v is not None:
                            return v
                    found = False
                    break
            for item in right:
                if item in left:
                    return None
                if not isinstance(item, Atom):
                    right.remove(item)
                    tup = item._tright(left, right)
                    left, right = tup[0]
                    if len(tup) > 1:
                        v = self._t(*tup[1])
                        if v is not None:
                            return v
                    found = False
                    break
            if found:
                return set(left)

    def t(self):
        return self._t([], [self])

    def to_cnf(self):
        def eliminate_implications(clause):
            if isinstance(clause, Atom):
                return clause
            args = None
            if isinstance(clause, Not):
                args = list(map(eliminate_implications, [clause.child]))
            else:
                args = list(map(eliminate_implications, [clause.lchild, clause.rchild]))
            a, b = args[0], args[-1]
            if isinstance(clause, Implies):
                return b | ~a
            if isinstance(clause, Iff):
                return (a | ~b) & (b | ~a)
            if isinstance(clause, And):
                return a & b
            if isinstance(clause, Or):
                return a | b
            if isinstance(clause, Not):
                return ~a

        def move_not_inwards(clause):
            if isinstance(clause, Not):
                def _not(c):
                    return move_not_inwards(~c)
                if isinstance(clause.child, Not):
                    return move_not_inwards(clause.child.child)  # ~~A => A
                if isinstance(clause.child, And):
                    return _not(clause.child.lchild) | _not(clause.child.rchild)
                if isinstance(clause.child, Or):
                    return _not(clause.child.lchild) & _not(clause.child.rchild)
                return clause
            if isinstance(clause, Atom):
                return clause
            if isinstance(clause, And):
                return move_not_inwards(clause.lchild) & move_not_inwards(clause.rchild)
            if isinstance(clause, Or):
                return move_not_inwards(clause.lchild) | move_not_inwards(clause.rchild)

        def distribute_and_over_or(clause):
            if isinstance(clause, Atom) or isinstance(clause, Not):
                return clause
            if isinstance(clause, Or):
                left_conj = dissociate(And, distribute_and_over_or(clause.lchild))
                right_conj = dissociate(And, distribute_and_over_or(clause.rchild))
                disjunctions = list(map(lambda el: el[0] | el[1], product(left_conj, right_conj, repeat=1)))
                return reduce(lambda a, b: a & b, disjunctions)
            if isinstance(clause, And):
                return distribute_and_over_or(clause.lchild) & distribute_and_over_or(clause.rchild)
            return clause

        if isinstance(self, Atom):
            return self
        s = eliminate_implications(self)
        s = move_not_inwards(s)
        return distribute_and_over_or(s)


class BinOp(Formula):
    def __init__(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '(' + str(self.lchild) + ' ' + self.op + ' ' + str(self.rchild) + ')'

    def __hash__(self):
        return hash(self.lchild) ^ hash(self.rchild) ^ hash(self.op)

    def eq(self, other):
        return self.lchild == other.lchild and self.rchild == other.rchild


class And(BinOp):
    op = '∧'

    def v(self, v):
        return self.lchild.v(v) and self.rchild.v(v)

    def _tleft(self, left, right):
        return (left + [self.lchild, self.rchild], right),

    def _tright(self, left, right):
        return (left, right + [self.lchild]), (left, right + [self.rchild])


class Or(BinOp):
    op = '∨'

    def v(self, v):
        return self.lchild.v(v) or self.rchild.v(v)

    def _tleft(self, left, right):
        return (left + [self.lchild], right), (left + [self.rchild], right)

    def _tright(self, left, right):
        return (left, right + [self.lchild, self.rchild]),


class Implies(BinOp):
    op = '→'

    def v(self, v):
        return not self.lchild.v(v) or self.rchild.v(v)

    def _tleft(self, left, right):
        return (left + [self.rchild], right), (left, right + [self.lchild])

    def _tright(self, left, right):
        return (left + [self.lchild], right + [self.rchild]),


class Iff(BinOp):
    op = '↔'

    def v(self, v):
        return self.lchild.v(v) is self.rchild.v(v)

    def _tleft(self, left, right):
        return (left + [self.lchild, self.rchild], right), (left, right + [self.lchild, self.rchild])

    def _tright(self, left, right):
        return (left + [self.lchild], right + [self.rchild]), (left + [self.rchild], right + [self.lchild])


class Not(Formula):
    def __init__(self, child):
        self.child = child

    def v(self, v):
        return not self.child.v(v)

    def __str__(self):
        return '¬' + str(self.child)

    def __hash__(self):
        return hash(self.child) ^ hash('¬')

    def eq(self, other):
        return self.child == other.child

    def _tleft(self, left, right):
        return (left, right + [self.child]),

    def _tright(self, left, right):
        return (left + [self.child], right),


class Atom(Formula):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def v(self, v):
        return self in v

    def __str__(self):
        return str(self.name)

    __repr__ = __str__

    def eq(self, other):
        return self.name == other.name


# region [ To cnf tests ]

def test_to_cnf():
    assert (~(a('B') | a('C'))).to_cnf().__str__() == '(¬B ∧ ¬C)'
    assert (a('P') >> (a('Q') & a('S'))).to_cnf().__str__() == '((Q ∨ ¬P) ∧ (S ∨ ¬P))'
    assert ((a('P') >> a('Q')) & a('S')).to_cnf().__str__() == '((Q ∨ ¬P) ∧ S)'
    assert ((a('P') & a('Q')) | (~a('P') & ~a('Q'))).to_cnf().__str__() == '((((P ∨ ¬P) ∧ (P ∨ ¬Q)) ∧ (Q ∨ ¬P)) ∧ (Q ∨ ¬Q))'
    assert (a('A') << a('B')).to_cnf().__str__() == '((A ∨ ¬B) ∧ (B ∨ ¬A))'
    assert (a('A') << ~a('B') >> (a('C') | ~a('D'))).to_cnf().__str__() == '(((((C ∨ ¬D) ∨ (¬A ∨ B)) ∧ ((C ∨ ¬D) ∨ (¬A ∨ A))) ∧ ((C ∨ ¬D) ∨ (¬B ∨ B))) ∧ ((C ∨ ¬D) ∨ (¬B ∨ A)))'

# endregion
