from sys import argv

script, file_name = argv

txt = open(file_name)
print "Here is your file %s" % file_name
print txt.read()

print "Enter the file name again:"
new_file = raw_input(">> ")
new_txt = open(new_file)
print new_txt.read()
