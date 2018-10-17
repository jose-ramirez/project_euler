# A row of five black square tiles is to have a number of its tiles replaced with
# coloured oblong tiles chosen from red (length two), green (length three), or
# blue (length four).
#
# If red tiles are chosen there are exactly seven ways this can be done. If green
# tiles are chosen there are three ways. And if blue tiles are chosen there are
# two ways.
#
# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing
# the black tiles in a row measuring five units in length.
#
# How many different ways can the black tiles in a row measuring fifty units in
# length be replaced if colours cannot be mixed and at least one coloured tile
# must be used?
#
# NOTE: This is related to problem 117.

def f(n):
    l = [0, 0, 1]
    if n <= 2:
        return l[n]
    else:
        i = 3
        while i <= n:
            l.append(l[i - 1] + l[i - 2] + 1)
            i += 1
    return l[n]

def g(n):
    l = [0, 0, 0, 1]
    if n <= 3:
        return l[n]
    else:
        i = 4
        while i <= n:
            l.append(l[i - 1] + l[i - 3] + 1)
            i += 1
    return l[n]

def h(n):
    l = [0, 0, 0, 0, 1]
    if n <= 4:
        return l[n]
    else:
        i = 5
        while i <= n:
            l.append(l[i - 1] + l[i - 4] + 1)
            i += 1
    return l[n]

print(f(50) + g(50) + h(50))