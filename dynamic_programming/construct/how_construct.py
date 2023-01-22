def how_construct(target, word_bank, memo=None):
    if len(target) == 0:
        return []  # Solution reached
    if memo is None:
        memo = {}
    elif target in memo.keys():
        return memo[target]
    for w in word_bank:
        if target.startswith(w):
            new_target = target.removeprefix(w)
            seq = how_construct(new_target, word_bank, memo)
            if seq is not None:
                memo[target] = [w] + seq
                return memo[target]
    memo[target] = None
    return None
# O((n^m)*m) time
# O(m^2) space


tests = [
    ('', ['ffg', 'gg', 'h']),
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
