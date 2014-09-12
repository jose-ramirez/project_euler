from utils import Utils

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
			print o
		#keep searching:
		o += 2

u = Utils()
u.exec_time(p46)