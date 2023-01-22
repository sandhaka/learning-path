def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target) + 1):  # m
        if len(table[i]) > 0:
            for word in word_bank:  # n
                if target[i:].startswith(word):  # m
                    for composition in table[i]:  # n^m
                        table[i + len(word)].append(composition + [word])
    return table[len(target)]
# O(n^m) time !!
# O(n^m) space


tests = [
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']),
    ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']),
    ('purple', ['purp', 'p', 'ur', 'le', 'purpl']),
    ('aaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])
]
for test in tests:
    print(all_construct(test[0], test[1]))
