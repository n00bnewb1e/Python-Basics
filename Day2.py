#Text is called a string in python

a = "This is a string"

#You can access every character of a string using [] square brackers

print(a[0])

#0 prints T
#1 prints h
#3 prints i.... and so on

#You can slice part of the string using the following

print(a[0:4]) #What will be the output?

#The above is called a indexing

#Indexing can also be negative. Like some pessimists.

print(a[-1]) #<------------ This prints the last character which is.... g
print(a[-1:-5]) #<---------- Guess what this will print

#To print the length of a string, which is the character count, use len() function

print(len(a))

b = " This is also a string but with spaces on the beginning and on the end "

print(b) #Well, this is gonna print the variable b, with spaces on the beginning and on the end
print(b.strip()) #This strips the whitespace from the variable b. See the difference? Good!

c = "almighty"

print(c.upper()) #Converts into UPPERCASE
print(c.lower()) #Converts into lowercase
print(c.capitalize()) #Capitalizes the first letter

d = "Duck"
print(d.replace("D", "B")) #Replaces D with B. SO you know what the output will be, you naughty mind!

e = "Politics"
print(e.split('l')) #Splits the string into two Po and itics

f = 2

g = "This is my day {}"
print(g.format(f))

# {} is a placeholder. Unlimited number of arguments can be places. More practice needed.

#What if you want to print this string Dwayne "The Rock" Johnson

# name = "Dwayne "The Rock" Johnson" will obviously give an error.
#The double quotes should start and end somewhere
#That's when escape character comes to the rescue \

name = "Dwayne \"The Rock \" Johnson"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Boolean

#Earth is Flat. True or False?

#You get the point. Boolean can either be true or False.
#1 < 10 True or False? Let's ask python

print(1 < 10)

#More practice needed

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Operators

#Add +
#Subtract -
#Multiply *
#Divide ------> will always return a float. What is int and what is float?
#Do you remember?

print(2 + 2) #Always evaluates to a single value

print(5 / 2)

#Well. This is simple. Can we do some complex stuff?
#Don't worry. That's for tomorrow. Just kidding. No complex stuff
