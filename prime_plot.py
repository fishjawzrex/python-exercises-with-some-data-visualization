'''THIS SCRIPTS PROMPTS THE USER FOR AN INPUT, AND THEN
PLOTS A HISTOGRAM/RELATIVE FREQUENCY CHART OF THE GAPS BETWEEN ALL THE PRIMES LESS
THAN THAT NUMBER'''
import prime_try as p 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp 


def prime_gaps(n):
	g = p.prime(n)
	 
	x = [0]
	for i in range(len(g)):
		if i > 0:
			x.append(g[i] - g[i-1])
	q = np.array(g)
	r = np.array(x)
	#plt.scatter(q,r, c='r', marker='o')
	plt.xlabel('prime_gap', color='gray')
	plt.ylabel('frequency', color='gray')
	plt.title('primes_gaps vs their relative frequency', fontsize=20, fontname="Times New Roman")
	plt.hist(r, bins='auto', normed=True, edgecolor='black', color='red', alpha=1)
	plt.grid(False)
	#plt.gca.set_facecolor('xkcd:salmon')
	w = np.mean(r)
	e = np.median(r)
	t = sp.mode(r)
	print "the mean of the distances is %d." % w
	print "the median is %d." % e 
	#print "the mode is %r." % t 
	plt.show()
	return g, x 

print "hey, enter a number that you \nwant the primes and gaps for:"
z = int(raw_input(">> "))
print prime_gaps(z)


