#In the 5 by 5 matrix below, the minimal path sum from the top left to the
#bottom right, by only moving to the right and down, is indicated in bold
#red and is equal to 2427.
#
#
#131	673	234	103	18
#201	96	342	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331
#
#Find the minimal path sum, in matrix.txt, a 31K text file containing a 80
#by 80 matrix, from the top left to the bottom right by only moving right
#and down.

from utils import Utils
u = Utils()

def p81():
    m = u.to_matrix('../data/matrix.txt', ',')
    rows = len(m)
    cols = len(m[0])
    mat = [[0 for j in range(cols)] for i in range(rows)]
    mat[0][0] = m[0][0]
    for i in range(1, cols):
        mat[0][i] += m[0][i] + mat[0][i - 1]
    for j in range(1, rows):
        mat[j][0] += m[j][0] + mat[j - 1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + m[i][j]
    return mat[rows - 1][cols - 1]

print p81()
