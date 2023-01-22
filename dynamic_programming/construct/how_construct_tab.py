def how_construct(target, word_bank):
    table = [None for _ in range(len(target) + 1)]
    table[0] = []
    for i in range(len(target) + 1):
        if table[i] is not None:
            for word in word_bank:
                if target[i:].startswith(word):
                    table[i + len(word)] = table[i] + [word]
    return table[len(target)]


tests = [
    ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']),
    ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    ('mind_blowing', ['nd', 'mind', 'w', 'blo', 'lo', 'ind', '_', 'wing', 'g', '_bl', 'ow', 'ing', 'mi']),
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
    print(how_construct(test[0], test[1]))
