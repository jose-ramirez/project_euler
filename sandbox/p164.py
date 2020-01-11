from time import time

def time_taken(f):
    def processing(n, k):
        start = time()
        r = f(n, k)
        end = time()
        print(f'f({n}, {k}) = {r}; Time taken: {end - start} seconds.')
    return processing

def validate(n,k):
    num_string = str(n)
    num_digits = len(num_string)
    digits = [int(n) for n in num_string]
    if num_digits < 3:
        return False
    else:
        for j in range(num_digits - 2):
            a, b, c = digits[j], digits[j + 1], digits[j + 2]
            if a + b + c > k:
                return False
        return True

@time_taken
def f(n, k):
    return sum([validate(m, k) for m in range(10 ** (n - 1), 10 ** n)])

for i in range(2, 7):
    f(i, 9)