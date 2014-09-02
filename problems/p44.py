from utils import Utils

def p44():
    u = Utils()
    limit = 3000
    pl = [u.pentagonal(i) for i in xrange(limit)]
    for a in xrange(1, limit):
        for b in xrange(1, limit):
            if a > b:
                c = pl[a] + pl[b]
                d = pl[a] - pl[b]
                if u.chop(c, pl) > -1 and u.chop(d, pl) > -1:
                    print a, b, pl[a], pl[b],\
                        pl[pl.index(c)],\
                        pl.index(c),\
                        pl[pl.index(d)],\
                        pl.index(d)

import time
start = time.time()
p44()
print time.time() - start