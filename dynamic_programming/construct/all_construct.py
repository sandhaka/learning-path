def all_constructs(target, word_bank, memo=None):
    if len(target) == 0:
        return [[]]  # Solution reached
    if memo is None:
        memo = {}
    elif target in memo.keys():
        return memo[target]
    allconstruncts = []
    for w in word_bank:
        if target.startswith(w):
            new_target = target.removeprefix(w)
            construncts = all_constructs(new_target, word_bank, memo)
            # Alternative with list - map:
            # allconstruncts.extend(list(map(lambda c: [w] + c, construncts)))
            for construnct in construncts:
                construnct = [w] + construnct
                allconstruncts.append(construnct)
    memo[target] = allconstruncts
    return allconstruncts


tests = [
    ('purple', ['purp', 'p', 'ur', 'le', 'purpl']),
    ('hello', ['cat', 'dog', 'cat', 'mouse']),
    ('', ['cat', 'dog', 'cat', 'mouse']),
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']),
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
    print(all_constructs(test[0], test[1]))
