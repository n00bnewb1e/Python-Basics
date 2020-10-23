#Day16

text = "{} is a placeholder text"
#{} is exactly a placeholder which means
#You can place whatever (string / int / float) in it's place

print(text.format("Lorem Ipsum")) #Use format() method
print(text.format(2)) #int placeholder
print(text.format(2.03)) #float placeholder
print(text.format({1, 2, 'e'})) #set placeholder
print(text.format((3, 4, 7))) #tuple placeholder.
print(text.format(['a', 2, 5, 'b'])) #list placeholder

print("++++++++++++++++++++++++++++++++++++++")

print("Fun fact: A bitcoin can be divided down to 8 decimal places.")
#What if we want to show 8 decimal places

btc_2009 = "{:.8f} was the block reward of bitcoin in 2009" #:.8f 8 floating digit values
print(btc_2009.format(50))

btc_2020 = "{:.8f} is the block reward of bitcoin as of 2020"
print(btc_2020.format(6.25))

btc_2032 = "{:.8f} will be the block reward of bitcoin in 2032"
print(btc_2032.format(0.78125))

#What if you want to display multiple values.

year = 2044
reward = 0.09765625

btc_supply = "In the year {}, the block reward will be {}"
print(btc_supply.format(year, reward))
#Notice, the order matters
print(btc_supply.format(reward, year)) #Run this, it doesn't make any sense

btc_2044 = "{} will be the block reward of bitcoin in {}"
print(btc_2044.format(reward, year))

btc_2056 = "{reward} will be the block reward of bitcoin in {year}"
print(btc_2056.format(reward = "0.01220703", year = "2056"))

#Notice the above line, with key, value pairs.
#Notice what's inside the placeholders too. IT's pretty self explanatory
#This is called named index

#Index can also be numbers

a = 'a'
b = 'b'
ab = "{}, {}"
print(ab.format(a, b)) #No problem right?

ab2 = "{0}, {1}"
print(ab2.format(a, b)) #Same as above, right?

ab3 = "{1}, {0}"
print(ab3.format(a, b)) #Guess what the answer will be?

print("##################################################")

#Python File Handling

sesame = open("ok.txt")
sesame1 = open("ok.txt", "rt") #RT means Russian Trolls? Heck no!
#r is read (default value)
#t is text (default value)
#So, both sesame and sesame1 is actually same
#The file that you're opening need to be present in the same directory of the py file

#Well, nothing happens. It just returns the file
#How to actually read the file and see the contents?
print(sesame.read())

sesame3 = open("Design.jpg", "rb") #Created a new folder named "Videos" and moved the mp4 file inside.
#You know r is read, what the buck is b?
#b is to read binary files, ex: images, videos, audios etc
print(sesame3.read()) #Brace yourself for some binary tsunami (depending on the size of the file)

#For the sake of simplicity, let's proceed with a txt file
#Just to add the context, following is the contents of my ok.txt file
"""ok.txt
abcde
abcde2
abcde3
abcde4
abcde5
"""

txt = open("ok.txt", "rt")

#What if you want to only read the first 4 characters from the file
#print(txt.read(4))

#What if you want to read the first line alone
print(txt.readline())
print(txt.readline()) #Display one more line from the txt file

#Loop through the file line by line using for

for x in txt:
    print(x)
    
#Make sure to properly close the file, unlike the programs on your windows

sesame.close()
sesame3.close()
txt.close()

print(type(txt)) #TextIOWrapper

txt = open("ok.txt", "rt")
#You know what rt is? read, text
#Do you know what a and w is? Aww....
#a is append (appends to the end of the file)
#w is write (overwrites existing content)

txt = open("ok.txt", 'a')
txt.write("adbc")
#print(txt.read()) #If you try to read it before closing, you will get
# 'io.UnsupportedOperation: not readable' error
txt.close()
# print(txt.read()) #Not too soon. You closed the file. You need to open it first. Remember? or you will get
# 'ValueError: I/O operation on closed file.' error

txt = open("ok.txt", 'r') #read
print(txt.read())
txt.close()

print("+++++++++++++++++++++++++++++++++++++++++++")

#overwrite with w

#txt2 = open("tk.txt", "r") #'io.UnsupportedOperation: not writable' error
txt2 = open("tk.txt", "w") #overwrite
txt2.write("Replaced all")
txt2.close()

txt2 = open("tk.txt", "r")
print(txt2.read())
txt2.close()

#Now, last, but not the least, x
#x creates a new empty file. If the file already exists, returns an error.

txt3 = open("hk.txt", "x")
#print(txt3.open()) #opening the empty file displays an error
#'AttributeError: '_io.TextIOWrapper' object has no attribute 'open'' error
txt3.close()

txt4 = open("ak.jpg", "x") #Create a file using x, and if the file already exists, returns an error
#'FileExistsError: [Errno 17] File exists: 'filname.ext'' error
txt4.close()

"""One more thing,
a (append) creates a new file as well, 
  even if the file does not exists,
  and does it's job, well, append
  
w (overwrite) creates a new file as well, 
  even if the file does not exists, 
  and does it's job. well, overwrite
"""

"""
Now, what's the syntax of open()
It accepts two parameters,
1.filename
2.mode (rawx) read / append / overwrite / create 
 (You can only use one at a time)
 (Try to use more than one at a time, and you will get an error)
"""
#txt5 = open("kk.txt", "rw") #two modes read and overwrite is used, you will get
#ValueError: must have exactly one of create/read/write/append mode

"""
Coming back to modes,
we also have
t (text)
b (binary)
that can be used along with one of rawx.
We've seen the example above in the line 76
"""