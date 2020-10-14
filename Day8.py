#Inheritance
#A wise man once told
#Money is either earned or inherited

'''So, we are going to create a parent and a child
and let's hopefully see how the child inherits
the parents' methods'''

#Let's create a parent first

class Ambani:
    def __init__(self, fname, net_worth):
        self.fname = fname
        self.net_worth = net_worth
        print("My name is ", fname, "Ambani",
        "and i am ", net_worth, "$ rich")

parent = Ambani('Dhirubai', '25B')

#Let's create a child and make it inherit from the parent Ambani

class Sons(Ambani): #See the difference?
    pass #Just pass it and it inherits every method from the parent
    
child = Sons('Mukesh', '50B')
child = Sons('Anil', '1B')

#See how the child inherited the method from Parent?

#If we initialize the child class using __init__()
#It won't inherit any property / method from the parent

'''Just like Kylie Jenner
This is how forbes put it.
Kylie Jenner Is Still The Youngest 
'Self-Made' Billionaire In The World

despite a lot of help from her famous family, 
she didn’t inherit her business
she built it'''

'''
Yeah, my mother built her
business from the ground up
with a million-dollar loan
from my grandfather. - Knives Out
'''

#So, if we initialize the child using __init__()
#It will no longer inherit the properties from the parent

class Daughters(Ambani):
    def __init__(self, name):
        self.name = name
        
        
print("+++++++++++++++++++++++++++++++++++++ Just a dummy separator")
child = Sons('Mukesh', '25B')
children = Daughters('Some') #See the difference?
print(children.name)

'''
The moment we initialize the class using __init__()
it will not inherit any properties / methods from the parent
However there's a catch!
super() function
'''

'''Use super() function with __init__() and it will 
still inherit the properties from it's parent'''

#So let's create a new parent
#New child
#and let's see super() in action

class Harlan:
    def __init__(self, fname, business):
        self.fname = fname
        self.business = business
        
    def fullname(self):
        print(self.fname + ' Thrombey')
        
class Linda(Harlan):
    def __init__(self, fname, business):
        super().__init__(fname, business)
        
    '''Be Sound mind and body
    We have defined lastname for the parent 'Harlan'
    We have not defined lastname for the child of Harlan, i.e, Linda
    But we used super()
    Which is gonna inherit all the properties of Harlan
    So,'''

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

a = Harlan('Harlan', 'Blood Like Wine Publishing')
print(a.fname)    #See, the init method requires print to display
print(a.business) 
a.fullname()    #A different function named 'fullname' requires () but not print

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

b = Linda('Linda', 'Real Estate')
print(b.fname)
print(b.business)
b.fullname() #See how Linda inherited things? We defined none of it for the child Linda.

#This is the power of super() function

