# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins. The
# result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer 
# rounded to seven decimal places in the form 0.abcdefg

from context import poly
def p205():
  peter = poly.Poly([1,1,1,1,0]).pow(9)
  colin = poly.Poly([1,1,1,1,1,1,0]).pow(6)

  total = 0
  for p in range(9, 37):
    for c in range(6, p):
      total += peter.coeff(p) * colin.coeff(c)
  return float(total) / ((4 ** 9) * (6 ** 6))

print(p205())