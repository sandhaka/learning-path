def count_construct(target, word_bank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1
    for i in range(len(target) + 1):  # m
        for word in word_bank:  # n
            if target[i:].startswith(word):  # m
                table[i + len(word)] += table[i]
    return table[len(target)]
# O((m^2)*n) time
# O(m) space


tests = [
    ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']),
    ('purple', ['purp', 'p', 'ur', 'le', 'purpl']),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'eee',
        'eeee',
        'eeeeee',
        'eeeeeeeee',
        'eeeeeeeeeeeee'
    ])
]
for test in tests:
    print(count_construct(test[0], test[1]))
