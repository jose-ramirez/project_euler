#Work out the first ten digits of the sum of the following one-hundred 50-digit
#numbers (in data/numbers.txt).

def p13():
    with open("data/numbers.txt", "r") as f:
        values = [int(v) for v in f.readlines()]
        return str(sum(values))[:10]

print(p13())