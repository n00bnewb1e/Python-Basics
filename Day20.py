#Day 20

from tkinter import * #From TkInter import everything

#abc = Tk() #Variable 'abc' is now a GUI if we use Tk()
#label = Label(abc, text = "Some Text") #You label abc with some text
#label.pack() #We pack the label.
#abc.mainloop()
'''
box = Tk()
a1 = Label(box, text = "ABC")
a2 = Label(box, text = "DEF")

#Now, instead of packing, we use grid, just like a spreadsheet
#grid has rows and columns

a1.grid(row = 0, column = 0) #When it comes to programming, everything starts with 0
a2.grid(row = 0, column = 1)
box.mainloop()
'''
#print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
'''
#Button

b = Tk()

def something():
    ans = Label(b, text = "I said Don't")
    ans.pack()
    
l = Button(b,                   #Refer the GUI and make it a button
text = "Don't Click Here",      #Give some text to the button
command = something,            #Command it to execute a function. Remember to NOT use ()
padx = 20,                      #Padding ------x----- horizontal (spacing)
pady = 20,                      #Padding y (Vertical) (spacing)
fg = '#ffffff',                 #fg ---> Foreground color
bg = '#000000')                 #bg ---> Background color
l.pack()                        #Pack it


#It does nothing. The reply you get when your girlfriend is mad at you.
#Now, obviosuly we need to make it do something
#Define the function before the button. Not After it.

b.mainloop()
'''

#Entry
main = Tk()
main.title("Calc")
a = Entry(main)                     #A text box to enter stuff
a.grid(row = 0,
column = 0,
columnspan = 3,
padx = 10,
pady = 10
#bg = "#000000" #_tkinter.TclError: 
# bad option "-bg": must be -column, 
# -columnspan, -in, -ipadx, -ipady, -padx, -pady, 
# -row, -rowspan, or -sticky
)

#b = Button(main, 
#text="Submit")
# b.pack()      #   _tkinter.TclError: 
# cannot use geometry manager pack inside . 
# which already has slaves managed by grid  

#b.grid(row = 1, column = 1)

def click(number):
    g = a.get()
    a.delete(0, END)
    a.insert(0, str(g) + str(number))

#Follow PEP 8 Style Guide

#Try NOT to use more than 79 characters in any line

#Also indent like the following
#Always use 4 spaces to indent. Not TAB.
a1 = Button(main, text = "1", command = lambda: click(1), 
            padx = 10, pady = 10).grid(row = 1, column = 0,)
            
#If lambda is not used, the value is filled by default
#Don't understand why?

a2 = Button(main, text = "2", command = lambda: click(2),
            padx = 10, pady = 10).grid(row = 1, column = 1,)
a3 = Button(main, text = "3", command = lambda: click(3),
            padx = 10, pady = 10).grid(row = 1, column = 2,)

a4 = Button(main, text = "4", command = lambda: click(4),
            padx = 10, pady = 10).grid(row = 2, column = 0,)
a5 = Button(main, text = "5", command = lambda: click(5),
            padx = 10, pady = 10).grid(row = 2, column = 1,)
a6 = Button(main, text = "6", command = lambda: click(6),
            padx = 10, pady = 10).grid(row = 2, column = 2)

a7 = Button(main, text = "7", command = lambda: click(7),
            padx = 10, pady = 10).grid(row = 3, column = 0)
a8 = Button(main, text = "8", command = lambda: click(8),
            padx = 10, pady = 10).grid(row = 3, column = 1)
a9 = Button(main, text = "9", command = lambda: click(9),
            padx = 10, pady = 10).grid(row = 3, column = 2)
                     
main.mainloop()