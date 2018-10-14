def binom(n):
    _m = [[1] + [0] * n, [1, 1] + [0] * (n - 1)]
    for m in range(2, (n + 1)):
        l = [1]
        for k in range(1, (n + 1)):
            c = _m[m - 1][k] + _m[m - 1][k - 1]
            l.append(c % 7)
        _m.append(l)
    return _m

def show_matrix(m):
    for line in m:
        print(line)

def count_in_matrix(m):
    total = 0
    for line in m:
        for n in line:
            if n % 7 != 0:
                total += 1
    return total

b = binom(99) # first 100 rows, which contain the first 5050 coefficients
print(f'total: {count_in_matrix(b)}')