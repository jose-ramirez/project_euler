from utils import Utils

def p(k):
  return 1 + k + (k * (k - 1)) / 2

def c(k, n):
  if n == 1:
    return 2 ** k - p(k)
  else:
    return c(k, n - 1) * (2 ** k) + ((2 ** k - p(k)) * (p(k) ** (n - 1)))

print [c(3, i) for i in range(1, 800)]
