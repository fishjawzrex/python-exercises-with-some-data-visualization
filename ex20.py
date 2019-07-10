from sys import argv

script, input_file = argv # this looks like it takes only one variable "input_file"

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


""" THE REWIND FUNCTION USES THE FILE.SEEK(0) 
	METHOD TO RETURN TO THE BEGINING OF 
	THE FILE. THE READLINE() READS ONLY 
	ONE LINE SETS THE POSTION TO THE END 
	OF THAT LINE.
"""