from fractions import gcd
from operator import itemgetter
import time

class Utils:
    """
        Calculates the binomial coefficient nCk.
    """
    def binom(self, n, k):
        m = [[0 for c in range (k + 1)] for r in range(n + 1)]
        #que diferencia hay entre esto y [[0] * (k + 1)] * (n + 1) ?
        #init:
        for i in range(n + 1):
            for j in range(k + 1):
                if i == j or j == 0:
                    m[i][j] = 1

        #calculating:
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                m[i][j] = m[i - 1][j - 1] + m[i - 1][j]
        return m[n][k]

    """
        Returns the sum of all numbers up to n.
    """
    def sum_up_to(self, n):
        return n * (n + 1) / 2
    #print(sum_up_to(100))

    """
        Returns a list with all fibonacci numbers up to m.
    """
    def fib(self, m):
        l = []
        l.append(0)
        l.append(1)
        f = 0
        while f < m:
            f = l[-1] + l[-2]
            if f < m:
                l.append(f)
        return l
    #print(fib(20))

    """
        Returns all primes less than n (if possible
        in a reasonable amount of time).
        Taken from
        http://code.activestate.com/recipes/577228-sieve-of-eratosthenes-python/
    """
    def sieve(self, n=100):
        sqrtn = int(n**0.5)
        sieve = [True] * (n+1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, sqrtn+1):
            if sieve[i]:
                m = n//i - i
                sieve[i*i:n+1:i] = [False] * (m+1)
        sieve = [i for i in range(n+1) if sieve[i]]
        return sieve
    #print(sieve(100))

    """
        Returns whether a word (assumed
        without whitespaces) is palindrome.
    """
    def palindrome(self, s):
        return s == s[::-1]
    #print(palindrome(str(998801)))

    """
        Returns the lcm of two numbers.
    """
    def lcm(self, a, b):
        return a * b / gcd(a, b)

    """
        Returns a matrix from the contents
        of a file (we're assuming it's
        possible anytime we call this function).
        TODO: this needs to be fixed to be able to read
        ALL the input files and returns a matrix with
        the data correctly.
    """
    def to_matrix(self, filename, separator = ' '):
        f = open(filename, 'r')
        #para llamar a las funciones de una clase dentro de ellas, usar self!:
        return [map(self.f1, row.strip('\n').split(separator)) for row in f.readlines()]
    #print(to_matrix('../data/mat.in'))

    """
        Prints a matrix to the screen.
    """
    def show(self, matrix):
        for row in range(len(matrix)):
            print(matrix[row])

    """
        Prints the matrix's dimensions, assuming all rows
        have the same length:
    """
    def size(self, name, matrix):
        print('%s\'s size: (%d, %d)' %(name, len(matrix),len(matrix[0])))

    """
        Returns a number representation of the number
        in a file (it's assumed that it's decimal
        representation is >= 100 digits).
    """
    def to_number(self, filename):
        return int(open(filename, 'r').readline())

    """
        Returns the number of divisors of n.
    """
    def d(self, n):
        i = 1
        res = 0
        while i ** 2 <= n:
            if n % i == 0:
                res += 2
                if n / i == i:
                    res -= 1
            i += 1
        return res

    """
        ... Still don't know if this is useful.
    """
    def f1(self, char):
        if char == '-':
            return 0
        else:
            return int(char)


    """
        Returns the value of x ** y (mod n), when x ** y
        is a really huge number, like 10 ** (10 ** 9).
    """
    def exp_mod(self, x, y, n):
        if y == 0:
            return 1
        z = self.exp_mod(x, y / 2, n)
        if y % 2 == 0:
            return (z ** 2) % n
        else:
            return (x * (z ** 2)) % n

    """
        Retorna el tiempo de ejecucion de la funcion que se le pasa como
        argumento en segundos.
        Pa la libreria; resvisar compatibilidad con versiones
        antiguas de python:
    """
    def exec_time(self, function):
        init = time.time()
        function()
        end = time.time()
        print("exec time: " + str(end - init) + " seconds")

class DisjointSet(dict):

    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]
        while self[parent] != parent:
            parent = self[parent]
        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]

class Algorithms:

    def kruskal(self, nodes, edges):
        forest = DisjointSet()
        mst = []
        for n in nodes:
            forest.add( n )
        sz = len(nodes) - 1
        for e in sorted( edges, key=itemgetter( 2 ) ):
            n1, n2, _ = e
            t1 = forest.find(n1)
            t2 = forest.find(n2)
            if t1 != t2:
                mst.append(e)
                sz -= 1
                if sz == 0:
                    return mst
                forest.union(t1, t2)
