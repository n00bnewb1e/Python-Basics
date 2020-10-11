#If you are alive
#Find me on Chimera

a = 33 #Define a variable a
b = 20 #Define another variable b

#if condition is pretty self explanatory
#Only thing is colon :
#and space (indendation) 

if a > b:
	print("A is greater than B")
elif a<b:
    print("A is less than B")
else:
    print("A is equal to B")
    
"""Be sure to change the values of A and B
and check if the code is working"""

#We can put everything in the same line too

print("A") if a > b else print("B")

#Here's a little long version

print("A") if a> b else print("Equal") if a==b else print ("B")

c = 70

if a > b and a > c:
    print("A is the largest number of all")
if a > b or a > c:
    print("A is definitely not the smallest number of all")

if a > 10:
    print("A is greater than 10")
    if a > 20:
        print("Also. A is greater than 20")
    else:
        print("and less than 20")
        
#if statement cannot be empty.
#In cases it need to be empty, use pass

if 10 > 5:
    pass
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#while loop

spy = 10

while spy < 100: #As long as the condition is true, the loop keeps on executing
    print(spy)
    spy +=1 #If we don't increment, the loop will continue forever
    
    
#Let's suppose if we want to break the loop at 50,
#The following code works

while spy < 100:
    print(spy)
    if spy == 50:
        break
    spy +=2
    
#What if we don't want to reach 50,
#Just jumble the code

while spy < 100:
    print(spy)
    spy +=2
    if spy ==50:
        break
    
#Let's know the usage of continue

while spy <100:
    spy +=3
    if spy == 22: #22 will be missing from the output
        continue
    print(spy)

'''Continue just tells python to continue the loop
without executing anymore code below
so it skipped print and hence no output of 22'''

#else also pairs with while

while spy < 20:
    print(spy)
    spy +=1
else:
    print("Spy is not 20 anymore")
    
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#for loop
char = ['sweet', 'big', 'red']
fruits = ['apple', 'banana', 'cherry']

#Both char and fruits are lists since we used [] square brackets
#Now we'll iterate the for loop

for x in char:
    print(x)
    
#We can also use a for loop inside a for loop

for x in char:
    for y in fruits:
        print(x,y)
        

#break is used to break the loop

for y in fruits:
    if y == "cherry":
        break
    print(y)
    

# continue is used to stop the current iteration and continue the loop

for y in fruits:
    if y == "banana":
        continue
    print(y)
    
#range can also be used in for loops

for xyz in range(10):
    print(xyz)
    
#The default value in range starts at 0.
#So, the numbers that'll be printed are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#That makes a total of 10 numbers. Isn't it?

for xyz in range(2, 10): #This starts the range at 2 and does not include 10
    print(xyz) #which is 2, 3, 4, 5, 6, 7, 8, 9
    
for xyz in range(2, 10, 2): #The third parameter 2 is the increment value. For example,. 2, 4, 6, 8
    print(xyz) #Guess what will be the output if the increment value is 3. Yes, it is 2, 5, 8
    
