import turtle


#Equilateral triangle

number = 100
angle = 120
tri = turtle.Turtle()
for x in range(0, 3):
    tri.forward(number)
    tri.left(angle)
turtle.done()

#print("+++++++++++++++++++++++++++++++++++++++++++")

'''
#Hexagon
number = 70
angle = 60
hex = turtle.Turtle()
for x in range(0, 6):
    hex.forward(number)
    hex.left(angle)
turtle.done()
'''

'''
#Sliced Hexagon
number = 70
angle = 60
sl_hx = turtle.Turtle()
sl_hx.pencolor("Blue")
for x in range(0, 6):
    sl_hx.forward(number)
    sl_hx.left(angle)
sl_hx.left(angle)

for y in range (0, 2):
    sl_hx.forward(number * 2)
    sl_hx.left(angle * 2)
    sl_hx.forward(number)
    sl_hx.left(angle * 2)
sl_hx.forward(number * 2)

turtle.done()
'''

'''
#Hexagon spider web
n = 150
m = 15
turn = 60
ins = 120
t = turtle.Turtle()
t.pensize(3)
color = ["#160C28", "#EFCB68", "#E1EFE6", "#000411", "#4D9DE0", 
"#E15554", "#E1BC29", "#3BB273", "#6D98BA"]

for x in range(1, 10):
    t.forward(n)
    t.left(turn)
    t.forward(n)
    t.left(turn)
    t.forward(n)
    t.left(turn)
    t.forward(n)
    t.left(turn)
    t.forward(n)
    t.left(turn)
    t.forward(n)
    t.left(ins)
    for z in range(0, 2):
        t.forward(n * 2)
        t.left(ins)
        t.forward(n)
        t.left(ins)
    
    t.forward(n * 2)
    t.backward(m)
    t.left(ins)
    t.pencolor(color[-x])
    n -= m
turtle.done()
'''

#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

'''
#Spiral
n = 70
ang = 10
color = ["#6D98BA", "#EFCB68", "#E1EFE6", "#000411", "#4D9DE0", 
"#E15554", "#E1BC29", "#3BB273", "#F1EFE6"]
c = turtle.Turtle()
c.pensize(2)
def circle():
    for x in range(0, 9):
        c.circle(n)
        c.left(ang)
        c.pencolor(color[x])
        
for y in range(0, 4):
    circle()
turtle.done()
'''
#print("#############################################")
'''
#Square spiral
len = 10
a = turtle.Turtle()
a.pensize(2)

while len < 96:
    a.forward(len)
    a.right(90)
    len += 4
turtle.done()
'''
'''
#Line of circles
color = ["#E15554", "#E1BC29", "#3BB273", "#F1EFE6"]
b = 50
c = 15
loc = turtle.Turtle()
loc.pensize(2)
def loci():
    for x in range(0, 3):
        loc.circle(b)
        loc.forward(c)
        loc.pencolor(color[x])
for x in range(0, 6):
    loci()
turtle.done()
'''