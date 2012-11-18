#2520 is the smallest number that can be divided by each of the
#numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?

import sys
sys.path.append('../utils')
from utils import lcm

def p5():
    return reduce(lcm, range(2, 21))

print p5()
    
