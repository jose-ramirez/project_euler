# Comparing two numbers written in index form like 2^11 and
# 3^7  is not difficult, as any calculator would confirm that
# 2^11 = 2048 < 3^7 = 2187.
#
# However, confirming that 632382^518061 > 519432^525806
# would be much more difficult, as both numbers contain over
# three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target
# As...'), a 22K text file containing one thousand lines with
# a base/exponent pair on each line, determine which line
# number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers
# in the example given above.

def p99():
    base_exp = open("data/p99_base_exp.txt", "r")
    number_list = base_exp.readlines()
    max_val = -1
    ind = 1
    max_ind = -1
    from math import log10
    for line in number_list:
        s = line.split(',')
        a, b = float(s[0]), float(s[1])
        d = b * log10(a)
        if d > max_val:
            max_ind = ind
            max_val = d
        ind += 1

    return max_ind

print(p99())