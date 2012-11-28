import sys
sys.path.append('../utils')
from utils import to_matrix, show

def p81():
    m = to_matrix('../data/matrix.txt', ',')
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
