def coll_length(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        l += 1
    return l

#print coll_length(13)

max_chain = -1
max_m = -1
for m in range(2, 10 ** 6):
    p = coll_length(m)
    if p > max_chain:
        max_chain = p
        max_m = m
print max_m, max_chain
