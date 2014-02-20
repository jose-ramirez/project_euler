#A number chain is created by continuously adding the square of the digits in a
#number to form a new number until it has been seen before.
#
#For example,
#
#44 -> 32 -> 13 -> 10 -> 1 -> 1 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4
#-> 16 -> 37 -> 58 -> 89
#
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless
#loop. What is most amazing is that EVERY starting number will eventually
#arrive at 1 or 89.
#
#How many starting numbers below ten million will arrive at 89?

"""
    Returns the sum of squares of the digits of n.
"""
def f(n):
    start = n
    total = 0
    while start >= 10:
        total += (start % 10) ** 2
        start = start / 10
    return total + start * start

"""
    It's still inefficient though.
"""
total = 0
max = 10 ** 7
for n in xrange(1, max + 1):
    x = n
    while f(x) != 1:
        x = f(x)
        if x == 89:
            total += 1
            break

print total