#Work out the first ten digits of the sum of the following one-hundred 50-digit
#numbers (in data/numbers.txt).

def p13():
    f = open("data/numbers.txt", "r")
    return str(sum(list(map(int, f.readlines()))))[:10]

print(p13())