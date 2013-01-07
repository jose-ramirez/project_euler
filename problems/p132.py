#A number consisting entirely of ones is called a repunit. We shall define R(k)
#to be a repunit of length k.
#
#For example, R(10) = 1111111111 = 11412719091, and the sum of these prime
#factors is 9414.
#
#Find the sum of the first forty prime factors of R(10^9).

from utils import utils
u = utils.Utils()


l = u.sieve(2 * (10 ** 5))

count = 0
total = 0
for p in l:
    if u.exp_mod(10, 10 ** 9, p) == 1:
        count += 1
        if count <= 41 and p != 3:
            total += p
            if count == 41:
                print total