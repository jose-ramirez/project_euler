# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

from math import sqrt

def p206():
  start = int('0'.join('1234567890'))
  for i in range(100000000):
    j = 1000 * int('0'.join(str(i)))
    m = int(sqrt(start + j))
    if(m ** 2 == test):
      return m

print(p206())