# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# The 12th term, F12 (144), is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
    Retorna el n-esimo numero de fibonacci, y solo a el.
    Para que retorne el arreglo completo hay que hacer
    unos cambios :p
"""
def fib(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

"""
    Retorna todos hasta el n-esimo numero de fibonacci,
    en una lista.
"""
def fib_list(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f

def p25():
    i = 4782
    n = fib(i)
    return i if len(str(n)) == 1000 else -1

print(p25())