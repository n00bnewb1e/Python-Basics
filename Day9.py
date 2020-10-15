#Iteration
#Repetition
#Repetition is the key

'''In python, iterator is an object
that iterates using
__iter__()
and __next__()'''

#Strings, Lists, Tuples, Sets, Dictionaries are all iterable objects

#We can't use next() without iter()
#iter() india
#next() nepal
a = [1, 2, 3, 4] #Is a list object.
b = iter(a) #Is made iterable using iter()
print(b) #Displays the memory location
print(next(b)) #Only if we use next(), it will display the value
print(next(b))
print(next(b))
print(next(b))
#print(next(b)) #We need to stop iteration at this point. You know why.
'''
No? Any more longer and python will display
Stop Iteration error.
Stop it. Just Stop it!
However, a for loop knows when to stop.
A genius knows when to stop!
'''

c = "Hakuna Matata" #Is a string.
d = iter(c) #Well, the short version is iter()
e = c.__iter__() #This is a long version. Both do the same thing. 

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print("")

print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print("Ex: Fill the Remaining")
print("")
#We can also iterate using for loop
for x in c:
    print(x)