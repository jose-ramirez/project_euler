import time
import math
from fractions import gcd
from operator import itemgetter
from math import sin, cos, atan, sqrt
import functools as ft
import euler.numbers.functions as f

class Utils:
    """
        Calculates the binomial coefficient nCk.
    """
    def binom(self, n, k):
        #que diferencia hay entre esto y [[0] * (k + 1)] * (n + 1)?:
        m = [[0 for c in range (k + 1)]
            for r in range(n + 1)]

        #init:
        for i in range(n + 1):
            for j in range(k + 1):
                if i == j or j == 0:
                    m[i][j] = 1

        #calculating:
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                m[i][j] = m[i - 1][j - 1] + m[i - 1][j]
        return m, m[n][k]

    """
        Returns the sum of all numbers up to n.
    """
    def sum_up_to(self, n):
        return n * (n + 1) // 2
    #print(sum_up_to(100))

    def fib(self, m):
        """
            Returns a list with all fibonacci numbers up to m.
        """
        l = []
        l.append(0)
        l.append(1)
        f = 0
        while f < m:
            f = l[-1] + l[-2]
            if f < m:
                l.append(f)
        return l

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

    def is_palindrome(self, s):
        """
            Returns whether a word (assumed
            without whitespaces) is palindrome.
        """
        return s == s[::-1]
    #print(palindrome(str(998801)))

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
        return [list(map(self.f1, row.strip('\n').split(separator)) )
            for row in f.readlines()]

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
        print('%s\'s size: (%d, %d)'
            %(name, len(matrix),len(matrix[0])))

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
                if n // i == i:
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
        z = self.exp_mod(x, y // 2, n)
        if y % 2 == 0:
            return (z ** 2) % n
        else:
            return (x * (z ** 2)) % n

    """
        Retorna el tiempo de ejecucion de la funcion que se
        le pasa como argumento en segundos. Pa la libreria;
        resvisar compatibilidad con versiones antiguas de
        python:
    """
    def exec_time(self, function):
        init = time.time()
        function()
        end = time.time()
        print("exec time: " + str(end - init) + " seconds")

    def chop(self, val, data):
        """
            Self made iterative binary search :)
            It is assumed that data is an ordered list. returns the
            index of val in data if val if found, else returns -1.
        """

        #the indices we'll be using to narrow our search:
        a, b = 0, len(data) - 1

        #we need to have enough data to make the testing:
        while b - a + 1 > 0:
            
            #update m to calculate the right address:
            m = b - a + 1

            #our suspect might be here in this position:
            pos = a + (m // 2)

            #found it! return the original index:
            if data[pos] == val:
                return pos

            #might be on the left side of the array:
            elif data[pos] > val:
                b = pos - 1

            #might be on the right side:
            else:
                a = pos + 1

        #here we also found nothing, since we ended up with a
        #pair of indices that can't be interpreted as the
        #extremes of an array:
        return -1

    """
        The nth hexagonal number.
    """
    def h(self, n):
        return n * (2 * n - 1)

    """
        Partition function, according to a recurrence due
        to Euler. Returns a list with all values of
        parts(k) for k up to n.
    """
    def parts(self, n):
        #initial values for parts(n):
        l = [1, 1, 2]
        i = 3
        for i in range(3, n + 1):
            #initial values for the indices:
            k, k_ = 1, -1
            total = 0
            ind = 0
            a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
            indices_valid = a >= 0 or a_ >= 0
            #calculate next value for partition function:
            while indices_valid:
                total += p_ * (l[a] * (a >= 0) + l[a_] * (a_ >= 0))
                #update indices:
                k, k_, ind = k + 1, k_ - 1, ind + 1
                a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
                indices_valid = a >= 0 or a_ >= 0
            #add value to list:
            l.append(total)
        return l

    """
        Cross product for 2d vectors, seen as 3d vectors with
        z component equal to 0.
    """
    def cross_2d(self, v1, v2):
        return [0, 0, v1[0] * v2[1] - v1[1] * v2[0]]

    """
        Dot product for arbitrary n-dimensional vectors.
    """
    def dot(self, v1, v2):
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    """
        Returns the vector joining points p1 towards p2.
    """
    def vec(self, p2, p1):
        return [p1[i] - p2[i] for i in range(len(p1))]

    """
        Returns True if points p1, p2 are on the same side of
        the line joining a and b.
    """
    def same_side(self, p1, p2, a, b):
        cp1 = self.cross_2d(self.vec(b, a), self.vec(p1, a))
        cp2 = self.cross_2d(self.vec(b, a), self.vec(p2, a))
        return self.dot(cp1, cp2) >= 0

    """
        Returns True if the point P is inside the triangle
        defined by t.
        Taken from the following page:
        http://www.blackpawn.com/texts/pointinpoly/
    """
    def in_triangle(self, p, t):
        a = t[0]
        b = t[1]
        c = t[2]
        return self.same_side(p, a, b, c) and\
            self.same_side(p, b, a, c) and\
            self.same_side(p, c, a, b)

    """
        Prime counting function. It depends on already having a
        precomputed list of primes.
    """
    def pi(self, n, prime_list):
        return bisect(prime_list, n) + 1

    """
        Counts all the semiprimes below n. Slows down as n
        becomes larger. Haven't proved whether the output
        is correct all the time or not:
    """
    def semiprimes(self, n):
        p_l = self.sieve(n)
        total = 0
        for p in p_l:
            if p < int(sqrt(n)) + 1:
                total += self.pi(int(n / p), p_l) - \
                    self.pi(p, p_l) + 1
            else:
                break
        print(total)

    #semiprimes(500000)

    """
      Dictionary with prime factors of m and its exponents:
    """    
    def divisors_dict(self, m, primes):
      vals = {}
      for p in primes:
        if m == 1:
          return vals
        if m % p != 0:
          continue
        else:
          m = m / p
          total = 1
          while m % p == 0:
            total += 1
            m = m / p
          vals.update({str(p): total})
      return vals

    """
        Matrix and vector product.
    """
    def mul(self, mat, vec):
        res = []
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            r = mat[i]
            res.append(sum([r[k] * vec[k] for k in range(cols)]))
        return res

    """
        Vector sum.
    """
    def add(self, v1, v2):
        return [v1[k] + v2[k] for k in range(len(v1))]

    """
        Vector difference.
    """
    def sub(self, v1, v2):
        return [v1[k] - v2[k] for k in range(len(v1))]

    """
        Matrix deifference.
    """
    def subm(self, m1, m2):
        m = []
        rows = len(m1)
        for i in range(rows):
            m.append(self.sub(m1[i], m2[i]))
        return m

    """
        Rotates the point p theta degrees centered at
        p0.
    """
    def rotate(self, p, p0 = [0, 0], theta = math.pi / 2):
        mat = [[cos(theta), sin(theta)], [-sin(theta), cos(theta)]]
        return self.add(self.mul(mat, self.sub(p, p0)), p0)

    """
        The idea here is to rotate a line, thus returning the
        parametric coefficients for x and y:
    """
    def rotate_line(self, m, b, r0, theta):
        M = [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]
        m_ = self.mul(M, m)
        N = self.subm([[1, 0], [0, 1]], M)
        b_ = self.add(self.mul(M, b), self.mul(N, r0))
        return m_, b_

    """
        Solve the quadratic equation ax^2 + bx + c = 0.
    """
    def solve_quadratic(self, a, b, c):
        d = sqrt((b ** 2) - (4 * a * c))
        return (-b - d) / (2 * a), (-b + d) / (2 * a)

    """
        Return line equation:
    """
    def get_line_equation(self, p, p0):
        mr = [1, (p0[1] - p[1]) / (p0[0] - p[0])]
        br = [0, p0[1] - (mr[1] * p0[0])]
        return mr, br

    """
        Return True iff p is in the line defined by m and b:
    """
    def is_in_line(self, m, b, p, tol = 1e-6):
        c1 = (p[0] - b[0]) / m[0]
        c2 = (p[1] - b[1]) / m[1]
        return abs(c1 - c2) < tol

    """
        Gets the coordinates of a point in a given line,
        and the parameter t that generates it.
    """
    def get_point(self,m, b, t):
        return [m[0] * t + b[0],
                m[1] * t + b[1]]

### Some testing for the geometry functions:
#multiply matrix and vector; result should equal [-1, 1]:
#print mul([[0 , -1], [1, 0]], [1, 1])
#
#subtract 2 matrices; should return [[0, 0], [0, 0]]:
#print subm([[1, 0], [0, 1]], [[1, 0], [0, 1]])
#
#rotate 90 degs counterclockwise, should print [1, 2]:
#print rotate([2, 1], [1, 1])
#
#get equation of rotated line; should return [-1, 1], [4, -2]
#print rotate_line([1, 1], [0, -2], [2, 0], math.pi / 2)

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

class Poly:
  def __init__(self, p):
    self.p = p
    self.deg = len(self.p) - 1

  def coeff(self, i):
    if i > self.deg:
      return 0
    else:
      return self.p[self.deg - i]

  def c(self, p2, r):
    total = 0
    if r == 0:
      return self.coeff(0) * p2.coeff(0)
    else:
      for i in range(r + 1):
        total += self.coeff(i) * p2.coeff(r - i)
    return total

  def mul(self, p2):
    l = [self.c(p2, i) for i in range(self.deg + p2.deg + 1)]
    return Poly(l[::-1])

  def pow(self, exp):
    if exp == 1:
      return self
    else:
      return self.mul(self.pow(exp - 1))
