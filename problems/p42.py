# The th term of the sequence of triangle numbers is given by t_n = \frac{n(n + 1)}{2};
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 15, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value. For example, the word value
# for SKY is 19 + 11 + 25 = 55 = t_{10}. If the word value is a triangle number then
# we shall call the word a triangle word.
#
# Using words.txt, a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?


from math import sqrt

def is_square(n):
    return int(sqrt(n + 0.5)) ** 2 == n

def is_triangular(t):
    return is_square(8 * t + 1)

def p42():
    with open('data/p042_words.txt') as input:
        total = 0
        words = [s.replace('"', '') for s in input.readline().strip().split(',')]

        for w in words:
            t = sum([ord(c) - 64 for c in w])
            if is_triangular(t):
                total += 1
        return total

print(p42())