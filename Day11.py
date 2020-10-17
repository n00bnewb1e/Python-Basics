#Day11 Module

#Create a separate file with name and py extersion
#For example converter.py
'''
The file needs to be present in the same directory(folder)
of the original py file that gets executed
or
place the file inside lib folder.
Don't know where the lib folder is?
Google is your friend. Ask her/him
'''

import converter #Imports the module converter
a = dir(converter) #dir() gets all the functions / variables inside the converter module
print(a) 

'''
Since we imported converter, to use it,
start with converter.name_of_the_function(parameter)
Examples below.
'''
converter.kg_to_lbs(70)
converter.lbs_to_kg(70)
converter.cm_to_ft(180)
converter.ft_to_cm(6)
converter.cm_to_inch(180)
converter.inch_to_cm(70)

converter.mile(5)

'''
What if we want only a single function from a module?
Importing the entire module is inefficient
because more lines of code,
more execution time,
more memory,
so, we can simply import a part of the module using
from
Example below
'''

from converter import inch_to_cm
#The above code only imports inch_to_cm

'''
Let's create a new module and do it!
Apart from a converter what's on your mind?
Take a break and you will get ideas!
Go for a walk
Do some exercise / yoga / meditation
Watch a movie
Relax
Sleep.
But be sure to come back here and
create something new
'''

