def factors(n): # generator that computes factors
	
	cache = []
	for k in range(1,n+1):
		if n % k == 0: # divides evenly, thus k is a factor
			cache.append(k)
			yield k 
			
			
			
			
print factors(100)