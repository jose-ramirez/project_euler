#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

from context import Utils
u = Utils()

def p3(n):
    p = u.sieve(7000)
    max = -1
    for q in p:
        if n % q == 0 and q > max:
            max = q
    return max

print(p3(600851475143))