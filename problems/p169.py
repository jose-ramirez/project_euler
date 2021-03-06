# Define f(0)=1 and f(n) to be the number of different ways n can be expressed as
# a sum of integer powers of 2 using each power no more than twice.
#
# For example, f(10)=5 since there are five different ways to express 10:
#
# 1 + 1 + 8
# 1 + 1 + 4 + 4
# 1 + 1 + 2 + 2 + 4
# 2 + 4 + 4
# 2 + 8
#
# What is f(10 ** 25)?

def f(n):
  if n < 2:
    return 1
  else:
    if n % 2 == 1:
      return f(n // 2)
    else:
      return f(n // 2) + f((n // 2) - 1)

def p169():
  a = f(5 ** 25)
  b = f(5 ** 25 -  1)
  return a + (25 * b)

print(p169())