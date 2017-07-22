filename = raw_input("Please input file name: ")

# Open the input file
txt = open(filename)

# File name
print "Here's your file %r:" % filename
# Open file
print txt.read()

txt.close()

# Try again
print "Type the filename again:"
# Prompt for the file name,give file_again assignment
file_again = raw_input(">")

# Open the file assigned to txt_again
txt_again = open(file_again)

# Print the file
print txt_again.read()

txt_again.close()