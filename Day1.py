#This is a comment

"""This
is
a
multi
line
comment"""

'''Either Single quotes
or double quotes
can be used for multi-line
comments'''

"""See it works
and python ignores
comments """

#Moving on to variables
#Think of variables like a box
#You can store things such as
#numbers, string(text), or complex
#Numbers can be int(3) or float(3.0)

#String(text) should be enclosed in quotes
#Whereas numbers should not have quotes

box = "variable"
box2 = 2

#Variable name can start with letters or underscores (_)
#Variable name cannot start with numbers
#Variable name can have numbers

print(box) # <------------ This code will display the text "variable"
print(box2) # <----------- Guess what the output will be?

#Multiple variables can be assigned in a single line

a, b = 2, 4

#a is now 2
#b is now 4

print(a, b)

a = b

#Guess what the values for a and b is?

#Both has become 4

print(b)
print(a)

c = 5j

#Guess what the type of c is?

print(type(c))

d = float(3)

print(d)

print(type(d))
print(type(a))
