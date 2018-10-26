# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

def p63():
  numbers = set()
  for n in range(1, 22):
    for a in range(1, 10):
      if (10 ** (n - 1)) <= a ** n < (10 ** n):
        numbers.add(a ** n)
  return len(numbers)

print(p63())