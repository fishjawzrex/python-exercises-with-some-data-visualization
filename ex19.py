def cheese_and_crackers(cheese_count, boxes_of_crackers): #THIS FUNCTION TAKES TWO ARGUMENTS
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
	
	
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
	
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
	
	
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
	
""" THE WHOLE POINT OF THIS EXERCISE WAS TO SHOW YOU 
	THE VARIOIUS WAYS YOU CAN PASS ARGUMENTS INTO A 
	FUNCTION; YOU CAN PASS THE NUMBERS IN DIRECTLY, OR 
	THROUGH PROXY VARIABLES IN OUR SCRIPT, WE CAN ALSO DO 
	MATH IN THE PARENTHESIS, AND, FINALLY, WE CAN 
	COMBINE THE TWO: WE CAN USE THE PROXY VARIABLES
	AND SIMULTENEOULSY ALTER THEM IN THE FUNCTION'S 
	PARENTHESIS WITH MATH!
"""