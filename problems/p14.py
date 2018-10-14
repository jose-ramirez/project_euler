#The following iterative sequence is defined for the set of positive integers:
#
#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains
#10 terms. Although it has not been proved yet (Collatz Problem), it is thought
#that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.

def coll_length(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        l += 1
    return l

def p14():
    max_chain = -1
    max_m = -1
    for m in range(2, 10 ** 6):
        p = coll_length(m)
        if p > max_chain:
            max_chain = p
            max_m = m
    return max_m, max_chain

print(p14())