ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #this shit naturally creates a list to put the split elements into
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy
print stuff.pop()
print ' '.join(stuff) #what? cool! This reverses what split does and changes shit from things in a list, separated by commas, into a string
print '#'.join(stuff[3:5]) # super stellar!