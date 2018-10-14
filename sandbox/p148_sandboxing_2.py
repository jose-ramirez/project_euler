from functools import reduce

def p_base(n, p):
    l = []
    if n == 0:
        return [0]
    while n:
        l.append(n % p)
        n = n // p
    return l

def T(m, p):
    b = p_base(m, p)
    inc_values = map(lambda x: x + 1, b)
    return reduce(lambda a, b: a * b, inc_values)

# verifying everything is ok (should print 2361):
# print(sum([T(m, 7) for m in range(100)]))

# exploratory test 1:
def block_level_1(i):
    """
        total between 49i and 49(i + i) - 1, i >= 0
    """
    return sum([T(m, 7) for m in range(i * 49, (i + 1) * 49)])

def block_level_2(i):
    return sum([block_level_1(m) for m in range(i * 7, (i + 1) * 7)])

def block_level_3(i):
    return sum([block_level_2(m) for m in range(i * 7, (i + 1) * 7)])

def block_level_4(i):
    return sum([block_level_3(m) for m in range(i * 7, (i + 1) * 7)])

def block_level_5(i):
    return sum([block_level_4(m) for m in range(i * 7, (i + 1) * 7)])

def block_level_6(i):
    return sum([block_level_5(m) for m in range(i * 7, (i + 1) * 7)])

print(sum([block_level_3(m) for m in range(7)]) - 28 * block_level_3(0))
print(sum([block_level_4(m) for m in range(7)]) - 28 * block_level_4(0))
print(sum([block_level_5(m) for m in range(7)]) - 28 * block_level_5(0))
print(sum([block_level_6(m) for m in range(7)]) - 28 * block_level_6(0))