def coeff(p, i):
  l = len(p)
  if i >= l:
    return 0
  else:
    return p[l - i - 1]

def c(p1, p2, r):
  total = 0
  if r == 0:
    return coeff(p1, 0) * coeff(p2, 0)
  else:
    for i in range(r + 1):
      total += coeff(p1, i) * coeff(p2, r - i)
  return total

def mul(p1, p2):
  l = [c(p1, p2, i) for i in range(len(p1) + len(p2) - 1)]
  return l[::-1]

def pow(p, exp):
  if exp == 1:
    return p
  else:
    return mul(p, pow(p, exp - 1))

def p205():
  peter = pow([1,1,1,1,0], 9)
  colin = pow([1,1,1,1,1,1,0], 6)

  total = 0
  for p in range(9, 37):
    for c in range(6, p):
      total += coeff(peter, p) * coeff(colin, c)
  return float(total) / ((4 ** 9) * (6 ** 6))

print(p205())