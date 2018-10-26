# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

from context import Utils

def p46():
	#getting precalculated primes and squares:
	u = Utils()
	primes = u.sieve(6000)
	squares = [i * i for i in range(1, 101)]
	#start searching at 15:
	o = 15
	while o < 5800:
		#is the test number prime?
		if u.chop(o, primes) != -1:
			#yeap, go to next one:
			o += 2
			continue
		#nope, begin testing:
		ind = 0
		found = False
		while o - primes[ind] > 0:
			s = (o - primes[ind]) / 2
			#found desired decomposition?
			if u.chop(s, squares) != -1:
				#yep, break out:
				found = True
				break
			#nope, try next prime:
			else:
				ind += 1
			#found possible candidate:
		if not found:
			return o
		#keep searching:
		o += 2

print(p46())