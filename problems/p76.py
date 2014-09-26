#It is possible to write five as a sum in exactly six
#different ways:
#
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
#
#How many different ways can one hundred be written as a sum
#of at least two positive integers?
#
from utils import Utils

u = Utils()

def p76():
    #we subtract 1 since we're only considering partitions
    #with more than one part:
    print u.parts(100)[-1] - 1

u.exec_time(p76)