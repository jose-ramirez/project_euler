#A row measuring seven units in length has red blocks with a minimum length of
#three units placed on it, such that any two red blocks (which are allowed to
#be different lengths) are separated by at least one black square. There are
#exactly seventeen ways of doing this.

#How many ways can a row measuring fifty units in length be filled?

def p114(n):
    l = [1, 1, 1, 2, 4]
    if n < 5:
        return l[n]
    else:
        i = 5
        while i <= n:
            l.append(l[i - 1] + sum(l[0:i - 3]) + 1)
            i += 1
    return l

print p114(50)[-1]
