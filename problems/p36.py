#The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in
#base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include
#leading zeros.)

from context import utils

u = utils.Utils()

def p36():
  total = 0
  for i in range(10 ** 6):
    if u.is_palindrome(str(bin(i)[2:])) and u.is_palindrome(str(i)):
      total += i

  return total

print(p36())