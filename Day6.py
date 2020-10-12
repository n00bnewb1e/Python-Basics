#Define a function using def

def some(): #some is the name of this function
	print('This is from a function') #which prints this
    
#Call the function using its name
#A function is executed only when it is called
some()

def name(fname): #The text inside brackets is called as a parameter
    print("Hello", fname) #Instead of ,(comma) +(plus / concatenation) can also be used
    
name('John') #The text inside parameter is called as an argument
name(1)
name("Toby")
name(1+8j) #Complex data type

#While defining, it is a parameter
#While calling, it is an argument

#If you specify 2 parameters, then 2 arguments need to be called

def person(fname, lname):
    print("Welcome", fname, lname)
    
#person("John") This will give an error since only one argument is called
#The correct code is

person("John", "Cena")
person("Triple", "H")
person("The", "Undertaker")

"""If you are not sure about the number of arguments
that you will be having with your spouse, look at the star in the sky"""

#If you are not sure about the number of arguments
#You need to add * before specifying the parameter
#While defining a function

def unknown(*name):
    print("The name is", name[-1])
    print(name[-2:])
    print(name[-3:])
    print(name[-4:])
    print(name[-5:])
    print(name[-6:])
    print(name[-7:])
    print(name[-8:])
    print(name[-9:])
    print(name[-10:])
    print(name[-11:])
    print(name[-12:])
    print(name[-13:])
    print(name[-14:])
    
'''def unknown(*name):
        print("The name is", name)
   
#Remove the comment,
and this code will display the entire name
irrespective of number of arguments.  
'''

"""
As you can see, the above code is repetitive and follows a pattern,
Now it ends at 10, but what if the number is 100.
You can write till 100 manually,
The purpose of any programming language is to automate,
To make computers work for us.

So, there has to be a better way of doing this.
But i don't know that yet.
I will rewrite this code once i know things.
As of now, just the manual method.
"""
    
unknown("Shriparwarmara", "Attapattu", "Jayasurya", "Lakshmana",
 "ShivaVenkata", "RajaShekhara", "Sriniwasana",
 "Trichipalli", "YekyaParampeel", "Parambatur",
 "ChinnaSwami", "MuthuSwami", "VenuGopala", "Iyer")
 
 
#Arguments can also be Key Value pairs

def eyes(e5, e9, e14):
    print("The E14 countries are", e14)
    
eyes(e14="UUCANDFHNGBISS", e5="UUCAN", e9="UUCANDFHN")

#Notice that the order of arguments don't matter this way

#If you have no idea the number of key value pairs
#Use ** before declaring a parameter inside the function
#Remember, it has to be key/value pairs
#Only the values don't work.
#For that, we have single star *

def cards(**Hearts):
    print("The number of cards are", Hearts)
    
cards(a=3, b=5, c=7, d=8, e='A', 
f='J', g='K', h=2, i=9, j=4, 
k='Q', l=9, m='A', n='7', o='K')

#We can set a default parameter,

def noob(language="python"):
    print("The programming language for noobs is", language)

noob() #This displays python as the answer, since it is the default value specified
noob('Javascript')

"""What? HTML is not on this list? 
Sorry. HTML has not yet made it 
to the list of programming languages."""

#Now, we have a list, we need to pass it to the function
#Guess what. It is possible.

chef = ['Gordan Ramsay', 'Thomas Keller', "Anne Sophie Pic", 
'Jamie Oliver', 'Dominique Crenn', 'Paul Pairet', 'Nadia Santini']
#See, i am all about equality
#But i couldn't find more lady chefs with a quick google search
#Tell me, and i will append the list

wwe_professionals = {'Alexa Bliss', 'Randy Orton',
'Becky Lynch', 'The Miz'}

#Attention to detail, my friend!
#wwe_professionals is a set. 
#We have used {} curly brackets
#Unordered and #Unindexed
#So wwe_professionals.append('Stephanie McMahon') wont work

actors = ['Tom Cruise', 'Tom Hanks',
'Jennifer Lawrence', 'Jennifer Aniston']

def function(*prof):
    for x in prof:
        print(x)
function(actors)
function(wwe_professionals)
function(chef)

actors.append('Jennifer Lopez') #How did i miss her?

function(actors) 

'''Since we have added * before prof
we tell python, we don't know the number of arguments,
so we can add as many actors, and there will be no error.'''


#return <---- Usage in w3schools
#I dont quite understand return
#I need to understand return
#The following code works too
def calc(num):
    print(10*num)
    
calc(5)
calc(10)

#Following is the code from w3schools for the same, but using return

def cal(number):
    return 10*number
    
print(cal(5))
print(cal(10))

#For some reason, if you prefer function to be empty, you can simply pass
#This way, you wont get an error

def test():
    pass
    
test()

#Practice Recursion