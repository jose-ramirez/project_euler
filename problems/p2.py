#Each new term in the Fibonacci sequence is generated by adding the
#previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not
#exceed four million, find the sum of the even-valued terms.

import euler.numbers.functions as f

def p2(m):
    a = f.fib(m)
    return sum([a[i] for i in range(len(a)) if a[i] % 2 == 0])

print(p2(4000000))