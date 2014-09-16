#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3
# + ... + 1000^1000.

from utils import Utils

def p48():
    print(sum([k ** k for k in range(1, 1001)]) % (10 ** 10))

u = Utils()
u.exec_time(p48)