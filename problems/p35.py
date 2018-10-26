#The number, 197, is called a circular prime because all
#rotations of the digits: 197, 971, and 719, are themselves
#prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11,
#13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

from context import Utils

def cyclic_shifts_of(str_num):
    m = len(str_num)
    i = 0
    l = [str_num]
    while i < m - 1:
        c = str_num[-1]
        str_num = str_num[:-1]
        c += str_num
        str_num = c
        l.append(c)
        i += 1
    return list(map(int, l))

def all_in(l1, l2, u):
    u = Utils()
    for n in l1:
        if u.chop(n, l2) == -1:
            return False
    return True

def p35():
    u = Utils()
    sieve = u.sieve(10 ** 6)
    count = 0
    for prime in sieve:
        s = str(prime)
        l = cyclic_shifts_of(s)
        if all_in(l, sieve, u):
            count += 1
    return count

def exec_():
    print(p35())

u = Utils()
u.exec_time(exec_)