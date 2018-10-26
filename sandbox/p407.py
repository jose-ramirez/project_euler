#chinese remainder theorem. To solve p407.py.

##Multiplicative inverse of a modulo n. Should be faster.
def mod_inv(a, n):
  for r in range(2, a):
    if (a * r) % n == 1:
      return r

def chr(pairs):
  N = 1
  x = 0
  for val in pairs:
    N *= int(val)

  for val in pairs:
    a = int(val)
    x += pairs[val] * (N // a) * mod_inv(N // a, a)

  return x % N, N

print(chr({"3": 2, "4": 3, "5": 1}))

#It is necessary for a, b to be relatively
#prime, so b can eventually be 1:
def r_q(a, b, r, q):
  if b == 1:
    return [r, q]
  else:
    r.append(a % b)
    q.append(a // b)
    return r_q(b, a % b, r, q)

print(r_q(244, 117, [], []))

def mod_inv_(a, n):
  r_q_ = r_q(a, n, [], [])
  r, q = r_q_[0], r_q_[1]
  a, b = -q[-1], (1 + q[-1] * q[-2])
  for i in range(-3, -(len(q) + 1), -1):
    a, b = b, a - b * q[i]
  return a, b

print(mod_inv_(244, 117))