#Day15 Exercises

#Ex1

text = ("Twinkle, twinkle, little star,\n" #escape \n for new line
 "\t How I wonder what you are! \n" #escape \t for tab or spaces
 "\t \t Up above the world so high,\n"
 "\t \t Like a diamond in the sky.\n"
 "Twinkle, twinkle, little star,\n"
 "\t How I wonder what you are") #Use these brackets and quotes in each line
 
 #That way, you can store multiple lines of the variable
 
print(text)

print("_+++++++++++++++++++++++++++++++++++++++++++++")

#Try Except

#Try for errors
#Except lets us handle the errors


#This is day15 of your journey! You might made a lot of mistakes!
#Do you remember any of them?
#Name an error please?
#Don't remember? It's totally ok!
#From now on, you are gonna keep track of every error
#Starting from now on
#Make a deliberate error

# print("ssd) #SyntaxError: EOL while scanning string literal

#Let's try except

try:
    print(abcd)
except:
    print("You made an error!") #You did not define a variable named abcd

print("++++++++++++++++++++++++++++++++++++")    
#Let's try except once more.

try:
    print(abcd)
except NameError:               #Notice any difference from previous except?
    print("What is the name of the error?")   #NameError occured, coz you did not define a variable using that name

print("+++++++++++++++++++++++++++++++++++++++++++++++++")    
#What if there is no error, use else

try:
    print("abcd2")
except NameError:
    print("Note the name of the error")
else: #If there's no error, else block gets executed
    print("Everything works fine")
    
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

#Finally, finally

try:
    print("abcd3")
except NameError:
    print("Miss me?")
else:
    print("No error")
finally: #This block gets executed regardless of error / no error
    print("Error or No error. finally gets executed")
    
#if you want to throw an error if some condition occurs,
#You can do so using raise
#Atleast, python gets a raise

a = 3
if a > 26:
    raise Exception("The number has to be less than or equal to 26")
