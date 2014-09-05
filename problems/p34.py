#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 =
#145.
#
#Find the sum of all numbers which are equal to the sum of
#the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not
#included.

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, xrange(1, n + 1))

def factorial_sum(n, factorial_list):
    total = 0
    while n >= 10:
        d = n % 10
        total += factorial_list[d]
        n /= 10
    return total + factorial_list[n]

#Hasta 10^6, porque ya se cuanto da la suma, y no necesito
#llegar tan lejos; pero en realidad hay que testar hasta
#10^7, que es lo que la matematica te da como estimado para
#estar seguro de que el resultado esta certo:
def p34():
    factorial_list = [factorial(n) for n in range(10)]
    total = 0
    for n in range(3, 10 ** 6):
        if n == factorial_sum(n, factorial_list):
            total += n
    return total

print p34()