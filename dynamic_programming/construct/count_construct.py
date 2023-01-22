def count_construct(target, word_bank, memo=None):
    if len(target) == 0:
        return 1
    if memo is None:
        memo = {}
    elif target in memo.keys():
        return memo[target]
    counter = 0
    for w in word_bank:
        if target.startswith(w):
            new_target = target.removeprefix(w)
            counter += count_construct(new_target, word_bank, memo)
    memo[target] = counter
    return memo[target]


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
