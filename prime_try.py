def prime(n):
	''' THIS FUNCTION USES THE SIEVE
	ALG. TO DETERMINE ALL PRIMES
	UP TO A GIVEN INPUT INTEGER
	'''
	cache = [] # create two identical empty lists
	cache_2 = []
	q = int(n**0.5) # we only need to compare up to the square root of n 
	for i in range(1,q):
		cache.append(int(i)) # append integers
	for j in range(1, n+1):
		cache_2.append(int(j))
	for a in cache:
		for b in cache_2:
			if a != b and b % a == 0:
				cache_2.remove(b)
	print "There are %d prime numbers between 0 and %s." % (len(cache_2), n) 
	return cache_2 #, len(cache_2), int(n)/len(cache_2)
#print prime(100)