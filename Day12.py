#Day12

import datetime

print(datetime.datetime.now())
print(dir(datetime))

x = [1, 2, 3, 4, 5]
print(min(x)) #Inbuilt math function to display the minimum number from an iterable
print(max(x)) #Inbuilt math function to display the maximum number from an iterable

#Next is a similar inbuilt math function called abs()
#Don't go working out already!
#It's called the absolute values
'''
If some number is positive, abs() will leave it the same
if some number is negative, abs() will make it positive
Better than Tony Robbins + Sandeep Maheswari Combined
'''

abc = -1
print(abs(abc)) #Guess what the result will be?

"""
Here's another example. But this time, we enclose it with () brackets
Remember, [] is for lists
{} is for sets
{} is for dictionary only if we use key:value pairs like
dictionary:thesaurus

It's the dino every kid is afraid of.

What is () for?
Yes, tuples

But, if we have only one value, it is not a tuple.
"""
xyz = (-102)
print(abs(xyz))
print(type(xyz))

"""
If we have more than one value, separated by a comma,
it qualifies as tuple
"""

zzz = (-102,)
print(type(zzz))

# print(abs(zzz)) <-------- abs() only applies to integers, not lists, tuples, sets or dictionaries

'''They say in movies
Don't underestimate the power of a common man
Well, python has power too.

pow(x, y) or
x**y

You may use whatever method,
But remember,
You've got the power
'''
q = pow(2, 8)
w = 2**8

print(q, w) #Yes, you can print two or more variables at once

#The builtin math functions are limited
#To extend this, python has a math library. Let's import it

import math

'''Square root of something is....
wait wait wait
I said square root, not square up.
'''

e = math.sqrt(256)
print(e)

#This one is to all the floor gang and ceiling gang around the world

floor = math.floor(10.36)
ceiling = math.ceil(10.36)
print(floor, ceiling) #See how it worked?

'''
Ceiling takes it up to rounds the number
Floor brings it down to round the number
'''

'''
Just finished watching the Creator games 2 hosted by Mr.Beast
Spoilers ahead:


D'Amelio family won the game
and almost everyone on the comments was saying
it was unfair that the family of 4 was competing against individual creators
But i beg to differ.
When asked what is the value of Pi, and coincidentally the slices of a Pie
Dixie D'Amelio cracked the answer and outsmarted everyone.

Of course she didn't put together all the numbers of Pi,
but since she got most of the letters right, she made it to the next rounds
and eventually answering the number of slices in a pie to win $300,000

You may ask how is this relevant?

Well, pi, pie and py

Python has a math function for pi.
'''

pie = math.pi #ATTN PLZZZZZZ NO BRACKETS for PI() <---- Shows 15 decimal points
print(pie)

c = math.pi * 2
print(c) #Yeah works

#Now we find out how close are you to your dog / cat / whatever
#Just kidding, works only with numbers,

d = math.isclose(1.2, 1.20000001) #Returns a True / False Value #Boolean\
b = math.isclose(1.2, 1.200000001)
print(d)
print(b)

'''
They say in movies,
Every man has a price (while bribing)
PS: Sorry to those who'll comment i din't include 'women' here

They're right.

Even python has a price. It takes just 7 extra zeroes.
6. No No. Doesn't count.
7. Yes.

See the answers above.
6 fraction zeroes, python tells you isclose() = False
7 zeroes and python changed it's mind. Now it's True.

#Perjury, your honor!

Even the slightest change in variable b,
Change the last 1 after 7 zeroes to 2
and python will tell you it's false for asking isclose()

Where to use isclose()?
I've no idea!
Will let you know if i ever use it again!
'''