#Work out the first ten digits of the sum of the following one-hundred 50-digit
#numbers (in data/numbers.txt).

def p13():
    f = open("../data/numbers.txt", "r")
    print str(sum(map(int, f.readlines())))[:10]

p13()
