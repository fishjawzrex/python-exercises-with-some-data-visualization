def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)
	
	
result = int(raw_input("Enter a Number: "))
facty = fact(result)
print "The factorial of the number you entered is %d" % facty