people = raw_input("\tDo you thing how many people in the world?\n\tPlease input: ")
cats = 20
dogs = 15


if not(people and cats):
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"

	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."