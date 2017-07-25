from sys import argv

script, input_file = argv

# read the file
def print_all(f):
	print f.read()

# go balck to the starting position of the file	
def rewind(f):
	f.seek(0)

# read the file line by line
def print_a_line(line_count, f):
	print line_count, f.readline(),

# assign the contents of a file to a variable
current_file = open(input_file)

print "First let's print the shole file:\n"

print_all(current_file)

print "Now let's rewing, kind of like a tape."	

# go black to the starting position of the file
rewind(current_file)

print "Let's print three lines:"

# print the first line
x = 1
print_a_line(x, current_file)

# print second line
x = x + 2
print_a_line(x, current_file)

# print the third line
x = x + 1
print_a_line(x, current_file)