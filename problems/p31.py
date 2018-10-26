#coding: UTF-8
#In England the currency is made up of pound, £, and pence, p, and there are
#eight coins in general circulation:
#
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

from math import floor

def p31():
  d = {}

  #1 and 2 coins (1c, 2c):
  for n in range(201):
    d[(1, n)] = 1
    d[(2, n)] = int(n / 2) + 1

  #3 coins (1c, 2c, 5c):
  for j in range(201):
    d[(3, j)] = d[(2, j)]
    for k in range(5, 201, 5):
      if j >= k:
        d[(3, j)] += d[(2, j - k)]

  #4 coins (1c, 2c, 5c, 10c):
  for j in range(201):
    d[(4, j)] = d[(3, j)]
    for k in range(10, 201, 10):
      if j >= k:
        d[(4, j)] += d[(3, j - k)]

  #5 coins (1c, 2c, 5c, 10c, 20c):
  for j in range(201):
    d[(5, j)] = d[(4, j)]
    for k in range(20, 201, 20):
      if j >= k:
        d[(5, j)] += d[(4, j - k)]

  #6 coins (1c, 2c, 5c, 10c, 20c, 50c):
  for j in range(201):
    d[(6, j)] = d[(5, j)]
    for k in range(50, 201, 50):
      if j >= k:
        d[(6, j)] += d[(5, j - k)]

  #7 coins (1c, 2c, 5c, 10c, 20c, 50c, 100c):
  for j in range(201):
    d[(7, j)] = d[(6, j)]
    for k in range(100, 201, 100):
      if j >= k:
        d[(7, j)] += d[(6, j - k)]

  #8 coins (1c, 2c, 5c, 10c, 20c, 50c, 100c, 200c):
  for j in range(201):
    d[(8, j)] = d[(7, j)]
    for k in range(200, 201, 200):
      if j >= k:
        d[(8, j)] += d[(7, j - k)]

  return d[(8, 200)]

print(p31())