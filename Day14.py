#Day14

#RegEx Module / Regular Expression
import re

text = "Lorem Ipsum is a dummy text used to display in web pages."

#search method is used to search for specific text
# ^ is a metacharacter
#Metacharacters are character with specific meaning
# ^ = starts with

x = re.search("^Lorem", text)
y = re.search("^lorem", text) #It's CaSe SeNsItIvE
print(x)
print(type(x))
#If there is a match is text, x returns class type re.Match
#If there is no match, it will return class type NoneType
print(y) #None
print(type(y)) #You know what the result will be? Don't you?

# $ = ends with
z = re.search("pages.$", text)
print(z)
#print(z) displays <class re.Match object; span=(string_index_start,string_index_end) match="pages.">

print(type(z))

#So far, we've covered start with(^) and end with($)
#There are a lot others. Seems Complicated!
#Learn 1 thing at a time

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#pip ---> Package installer for Python
#it contains all the packages / modules
#If you're running python 3.4 or above, pip comes by default
'''
Remember, pip is accessible only via cmd / shell. 
Not in idle / ide.
Make sure to run cmd as admin.
Check if pip is installed or not,
First, navigate to Scripts folder of python in cmd / shell
pip --version
'''

#Upgrade to the latest version of pip using
#pip install --upgrade pip

#Downloading a package from pip is very easy
#Just use the command (pip install package_name)
#You need to do it from a cmd in scripts folder
#For example
#pip install camelcase

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import camelcase #CamelCase ThisIsCamelCaseInPythonAndOtherLanguagesIncludingJavascript
print(dir(camelcase))

abc = camelcase.CamelCase()
a1 = abc.hump(text) #use the hump method. Don't ask me why? I dont know it yet
print(a1)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pyperclip #Clipboard data
b1 = pyperclip.paste() #Paste what was in the clipboard
print(b1)

#w1 = pyperclip.waitForNewPaste() #Uncomment w1 variable and see how it works
#print(w1) #Don't forget to uncomment this line too

c1 = pyperclip.copy("New text") #Replaces the clipboard data to "New text"
d1 = pyperclip.paste()
print(d1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import emoji #Yes, emoji
print(dir(emoji))
print(emoji.emojize(":last_quarter_moon:")) #use emojize method

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

'''
Intall howdoi using pip and you can ask questions such as
howdoi make a list
Remember, you have to do it from cmd
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import wikipedia #Our free encyclopedia
print(dir(wikipedia))
wk0 = wikipedia.random()
print(wk0)
wk = wikipedia.summary(wk0)

wk1 = wikipedia.search("Python")
print(wk1)