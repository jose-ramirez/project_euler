#Using a combination of black square tiles and oblong tiles
#chosen from red tiles measuring two units, green tiles
#measuring three units, and blue tiles measuring four units,
#it is possible to tile a row measuring five units in length
#in exactly fifteen different ways.
#
#How many ways can a row measuring fifty units in length be
#tiled?
#
#NOTE: This is related to Problem 116.

from utils import Utils

u = Utils()

def p117():
    l = [0, 1, 2, 4, 8]
    for i in range(5, 51):
        l.append(l[-1] + l[-2] + l[-3] + l[-4])
    print l[-1]

u.exec_time(p117)