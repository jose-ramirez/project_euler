#Triangle, pentagonal, and hexagonal numbers are generated
#by the following formulae:
#
#Triangle Tn = n(n + 1)/2: 1, 3, 6, 10, 15, ...
#Pentagonal Pn = n(3n - 1)/2: 1, 5, 12, 22, 35, ...
#Hexagonal Hn = n(2n - 1): 1, 6, 15, 28, 45, ...
#
#It can be verified that T_285 = P_165 = H_143 = 40755.
#
#Find the next triangle number that is also pentagonal and
#hexagonal.

from context import f

def p45():
    a, b = 1, 1
    i = 0
    h_, k_, r_ = 0, 0, 0
    while i < 3:
        a, b = 2 * a + 3 * b, a + 2 * b
        if a % 6 == 5 and b % 2 == 1:
            #triangular:
            h_ = (b - 1) // 2
            #pentagonal:
            k_ = (a + 1) // 6
            if h_ % 2 == 1:
                #hexagonal:
                r_ = (h_ + 1) // 2
                i += 1
    return f.t(h_)

print(p45())