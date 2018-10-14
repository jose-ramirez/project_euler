# A perfect number is a number for which the sum of its proper divisors
# is exactly equal to the number. For example, the sum of the proper
# divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.

# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundant
# numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this
# limit.

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

def get_abundants(n):
    abundants = []
    with open('data/abundants.txt', 'r') as abundants_txt:
        return list(map(int, abundants_txt.readlines()[0].split(', ')))

abundants = get_abundants(28123)

# First correct solution :)
# def p23_1():
#     s = set()
#     for i in range(len(abundants)):
#         for j in range(i, len(abundants)):
#             s.add(abundants[i] + abundants[j])
#     l1 = [m for m in s if m <= 28123]
#     print(395465626 - sum(l1))

# 2x faster than p23_1() :p
def p23():
    bools = [False for i in range(56247)]
    for i in range(len(abundants)):
        for j in range(i + 1):
            bools[abundants[i] + abundants[j]] = True
    l1 = [m for m in range(len(bools)) if (not bools[m] and m < 21000)]
    return sum(l1)

print(p23())