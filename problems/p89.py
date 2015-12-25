#For a number written in Roman numerals to be considered valid there are basic
#rules which must be followed. Even though the rules allow some numbers to be
#expressed in more than one way there is always a "best" way of writing a
#particular number.
#
#For example, it would appear that there are at least six ways of writing the
#number sixteen:
#
#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI
#
#However, according to the rules only XIIIIII and XVI are valid, and the last
#example is considered to be the most efficient, as it uses the least number of
#numerals.
#
#The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
#contains one thousand numbers written in valid, but not necessarily minimal,
#Roman numerals; see About... Roman Numerals for the definitive rules for this
#problem.
#
#Find the number of characters saved by writing each of these in their minimal
#form.

#Note: You can assume that all the Roman numerals in the file contain no more
#than four consecutive identical units.

numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

huns = {0:"", 100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM"};
tens = {0:"", 10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC"};
ones = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"};



def roman2num(roman_num):
  last_numeral = roman_num[-1]
  rom = roman_num[:-1]
  total = numerals[last_numeral]
  for numeral in rom[::-1]:
    if numerals[numeral] >= numerals[last_numeral]:
      total += numerals[numeral]
    else:
      total -= numerals[numeral]
    last_numeral = numeral
  return total

#print roman2num("MDCCCCLXXXXVIIII")
#print roman2num("MCMXCIX")

def num2roman(number):
  str = ""
  n = number
  while n > 1000:
    n -= 1000
    str += "M"
  str += huns[n - (n % 100)]
  str += tens[(n % 100) - (n % 10)]
  str += ones[n % 10]
  return str

#print num2roman(1999)
#print num2roman(2527)
#print num2roman(5469)

def p89():
  romans = open("../data/p089_roman.txt", "r")
  total = 0
  for line in romans.readlines():
    total += len(line.strip()) - len(num2roman(roman2num(line.strip())))
  return total

print p89()
