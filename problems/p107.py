#A network can be represented by the matrix below.
#
#    	A	B	C	D	E	F	G
#A	-	16	12	21	-	-	-
#B	16	-	-	17	20	-	-
#C	12	-	-	28	-	31	-
#D	21	17	28	-	18	19	23
#E	-	20	-	18	-	-	11
#F	-	-	31	19	-	-	27
#G	-	-	-	23	11	27	-
#
#However, it is possible to optimise the network by removing some edges and
#still ensure that all points on the network remain connected. The network
#which achieves the maximum saving is shown below. It has a weight of 93,
#representing a saving of 243  93 = 150 from the original network.
#
#
#Using network.txt (right click and 'Save Link/Target As...'), a 6K text
#file containing a network with forty vertices, and given in matrix form,
#find the maximum saving which can be achieved by removing redundant edges
#whilst ensuring that the network remains connected.

import sys
sys.path.append('../utils')
from utils import to_matrix, show
from kruskal import kruskal

def f1(r):
    a = r.split(',')
    return [f2(x) for x in a]

def f2(p):
    if p == '-' or p == '-\n':
        return 0
    else:
        return int(p)

def get_aristas(mat):
    return [[i, j, mat[i][j]] for i in range(len(mat))
        for j in range(len(mat[0])) if mat[i][j] != 0]

def p107():
    lines = open('../data/network.txt').readlines()
    adj_mat = [f1(row) for row in lines]
    total = sum([sum(adj_mat[i]) for i in range(len(adj_mat))]) / 2
    #show(adj_mat)
    nodos = range(len(adj_mat))
    aristas = get_aristas(adj_mat)
    arbol = kruskal(nodos, aristas)
    s = sum([arbol[i][2] for i in range(len(arbol))])
    return total - s


print p107()
