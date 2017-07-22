from sys import argv

script, first, second, third, fourth = argv

# argv = raw_input('Please enter five varibales: ')

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

x = raw_input("Please enter one number: ")
y = int(x)
print ("%r") % (y * 2)