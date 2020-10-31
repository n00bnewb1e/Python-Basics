#Day 19

'''
n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
    
if n % 2 == 0 and n >= 2 and n < 5:
    print("Not Weird")

if n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")

if n % 2 == 0 and n > 20:
    print("Not Weird")
    
'''
'''
n = int(input())
for x in range(0, n):
    print(n * n)
    n += 1
'''
'''
def is_leap(year):
    if year % 4 == 0:
        return True
        if year % 400 == 0:
            return True
    if year % 4 == 0 and year % 100 == 0:
        return False
    return leap

year = int(input())
'''
#Dictionary
'''abc = {}
abc['a'] = 1
abc['b'] = 2
abc['c'] = 3
abc['d'] = 4
abc['e'] = 5
abc['f'] = 7
abc[3] = 8
print(abc)
'''

#Requests library
#import requests
#r = requests.get("https://www.twitter.com")

#import tkinter
#gui = tkinter.Tk() #The first letter in Tk has to be CAPS
#gui.mainloop() #Main loop

#import tkinter
#gui = tkinter.Tk()
#gui.geometry('300x300') #Resolution of the box
#f = Frame(gui) # NameError: name 'Frame' is not defined
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

#TkInter Library
#What is TkInter.
#Tk ---------> Toolkit
#Inter ------> Interface
#Now you know it
#You need to import everything from tkinter
#How do you do that?

from tkinter import * #(*) means everything when it comes to most programming languages
g = Tk() #Make the variable 'g' into a toolkit
l = Label(g, text = "yu") #Label 'g' with a text
l.pack() #Pack everything
ll = Label(g, text = "game").pack() #Pack everything in a single line
g.mainloop() #Loop with mainloop() #Some say it tracks mouse movements