#The line below uses the %d formatter to call the numer 10 into the string"
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Line 6 basically does the same thing as line 2, but this time, it calls two string variables instead of one."
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y 
# Lines 11 and 12 print the nested strings
print "I said: %r." % x 
print "I also said: '%s'." % y 
# 14 and 15 show a good example of when to use the %r formatter.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# printing nested strings again.
print joke_evaluation % hilarious
# CONCATENATION!
w = "This is the left side of..."
e = "a string with a right side."

print w + e 