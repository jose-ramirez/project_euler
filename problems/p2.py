import sys
sys.path.append('../utils')
from utils import fib

def p2(m):
    a = fib(m)
    return sum([a[i] for i in range(len(a)) if a[i] % 2 == 0])

print p2(4000000)
