from sys import argv

script, filename = argv

txt = open(filename, 'r')

print "This is just write the file content: %r" % filename

print txt.read()