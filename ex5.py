# -*- coding: utf-8 -*-
name = u'王小二'
age = 27 # not a lie
height = 165 # centimeter
weight = 112 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %.2f inches tall." % (height * 0.39)
print "He's %.2f pounds heavy." % (weight * 2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)