#This is a lambda function
#A lambda can have any number of arguments
#But only one expression i.e, that is evaluated
#For example
#Syntax is lambda arguments : expression

#The following code has only one argument
x = lambda a : a + 10
print(x(10))

#Any number of arguments can be added to the lambda
y = lambda a, b: a + b+15
print(y(6,6))

print(type(x)) #The type is function
print(type(y)) #The type is function

#Since this function doesn't have a name,
#Lambda is called as an anonymous function


#But why use lambda function?
'''Use lambda function when an 
anonymous function is required
for a short period of time'''

#++++++++++++++++++++++++++++++++++++++++++++++++++

#Python Class

#Python is an object oriented programming language
#What that means is.......
#They say, Women are not objects
#In the eyes of python, we all are objects

#Create a class using class

class Students: #It is a convention to capitalize the first letter of the class
    pass #It should not be empty.
    #It has to have a value,
    #and to eliminate errors, we pass


adam = Students()

'''
Adam is an object here
since we assign it to the class Students
It should end with ()
'''
print(adam) #Displays the object

'''
We can attach attributes to adam
such as height, weight, age, etc
using dot(.)

While creating an email ID,
Gmail considers adam.eve@gmail.com
and adameve@gmail.com as the same.
Remember?
It's not even relevant.
Don't know why i mentioned that.
'''

adam.age = 20 #Attach attributes using dot(.)
adam.height = 180 #cm
adam.weight = 180 #pounds
adam.email = 'adameve@gmail.com'

print(adam.age)
print(type(adam.age))

#Now if we want to create the same for Eve,
#We need extra 4 lines of code.
#and for each new 

eve = Students() #Add eve to students or python will give a error

eve.age = 18 
eve.height = 160 #cm
eve.weight = 160 #pounds
eve.email = 'eveadam@gmail.com'

#It's very simple form of class and object
#To get to know these better
#To use them in real-world apps,
#we need to understand the built-in __init__() function


#Let's create a class for youtubers
#This time, instead of pass
#We are actually creating a function

class Youtubers():
    '''If we define a function inside a class
    we need to initialize it using __init__() function
    
    It has the text init and two underscores on each side
    Just like the security given to Kim Jong Un
    
    So it's __init__()
    Let's define it. Shall we?
    
    def __init__():  <----- This is called a method coz it's inside a class
    ---> Now, inside the brackets,
    We need to add arguments,
    By default, first argument in the method is an instance
    For instance,
     To find fortune and riches 
     one doesnt need help. 
     All one has to do is look to one self.
     Thanks to The Mentalist.
    By Convention, python programmers use self.
    And. Also Document. It helps a loooong way.'''
    '''
    Dummy second documentation
    '''
    def __init__(self, name, followers):
        self.name = name
        self.followers = followers 
    
    def theme(self):
        self.idea = idea
        
#help(Youtubers) 
#Displays the first documentation written within triple quotes.
#The second documentation is not visible

pewdiepie = Youtubers('Pewdiepie', '106M') #In the same order
print(pewdiepie.followers)

mrbeast = Youtubers('MrBeast', '50M')
print(mrbeast.name)

jacksucksatlife = Youtubers("JackSucksAtLife", '2M')
print(jacksucksatlife.name)

mrbeast.theme = "Money"
print(mrbeast.theme)

'''Basically, OOP or Object Oriented Programming
promotes code re-use
eliminating unnecessary code'''