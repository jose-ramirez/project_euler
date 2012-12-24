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

print p114(50)
