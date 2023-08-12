#new items 15 dec 2022
#format shape

import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
h = 0
def draw(ang,n):
    t.circle(5+n,60)
    t.left(ang)
    t.circle(5+n,60)
t.pensize(5)
t.goto(0,0)
for i in range(250):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.016
    t.pencolor(c)
    t.fillcolor('black')
    t.begin_fill()
    draw(90,i*0.05)
    draw(160,i*1.2)
    t.end_fill()
    t.up()
    draw(180,i)
    draw(90,i*2)
    t.down()
t.done()
    

# #new items 15 dec 2022
# #graphic Design

# import turtle as t
# import colorsys
# t.bgcolor('black')
# t.pensize(2)
# t.speed(500000)
# h=0.4
# t.up()
# t.goto(0,100)
# t.down()
# for i in range(260):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     h +=0.002
#     t.color(c)
#     t.up()
#     t.fd(i*2)
#     t.down()
#     t.circle(i,-150)
#     t.fd(i)
#     t.circle(i,-150)
# t.done()


# #new items 15 dec 2022
# #graphic Design

# import turtle as t
# import colorsys
# t.bgcolor('black')
# t.pensize(2)
# t.speed(0)
# h=0.4
# t.up()
# t.goto(0,100)
# t.down()
# for i in range(260):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     h +=0.002
#     t.color(c)
#     t.up()
#     t.fd(i*2)
#     t.down()
#     t.circle(i,-100)
#     t.fd(i)
#     t.circle(i,-100)
# t.done()



# #new items 15 dec 2022
# #graphic design

# from turtle import*
# import colorsys
# bgcolor('black')
# tracer(50)
# h=.4
# for i in range(180):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     h +=0.018
#     width(i//100+1)
#     pencolor(c)
#     fillcolor(c)
#     left(59)
#     begin_fill()
#     forward(i*0.5)
#     circle(i*0.3)
#     end_fill()
#     right(90)
#     forward(i*1.5)
#     circle(i,90)
# done()



'''#Q1. opening

from turtle import*
color ('red','yellow')
bgcolor('black')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()


#Q2. Doyel's Code

from turtle import*
import colorsys
speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)
h=0.001
for i in range(90):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)
    h+=0.02
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h+=0.02'''




#Q3. Normal flower

from turtle import*
import turtle

bgcolor('black')
pensize(2)
color('green')
left(90)
backward(100)
ht=(100)
speed(50000)
shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        forward(i)
        color( 'orange')
        circle(2)
        color('brown')
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)
tree(100)
turtle.done()


#Q4. DELL Logo

import turtle

t=turtle.Turtle()

t.pensize(15)
t.color("#3287c1","#3287c1")
t.penup()
t.goto(20,-200)
t.pendown()
t.circle(180)
t.penup()


'''#Draw the "D" of the DELL logo
t.pensize(2)
t.goto(-130,-70)
t.pendown()
t.setheading(90)
t.forward(90)
t.right(90)
t.forward(50)
t.penup()
t.goto(-130,-70)
t.setheading(0)
t.pendown()
t.forward(50)
t.left(10)
t.circle(46,165)
t.penup()

t.color("#3287c1")
t.goto(-130,-70)
t.setheading(0)
t.pendown()
t.begin_fill()

t.forward(20)
t.left(90)
t.forward(90)
t.left(90)
t.forward(20)
t.end_fill()
t.backward(20)
t.left(90)
t.forward(17)
t.setheading(0)
t.begin_fill()
t.forward(30)
t.right(25)
t.circle(-30,130)
t.setheading(180)
t.forward(30)
t.left(90)
t.forward(17)
t.setheading(0)
t.forward(30)
t.left(10)
t.circle(45,165)
t.setheading(180)
t.forward(47)
t.end_fill()
t.penup()

#Draw the 'E' of the DELL logo
t.goto(-45,-15)
t.pendown()
t.setheading(0)
t.left(35)
t.begin_fill()
t.forward(65)
t.right(90)
t.forward(18)
t.right(90)
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.forward(18)
t.right(90)
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.forward(18)
t.right(90)
t.forward(65)
t.right(85)
t.forward(65)
t.penup()
t.end_fill()

#Draw the 'L' of the DELL logo
t.goto(40,-70)
t.setheading(90)
t.pendown()
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()
t.penup()

#Draw the 'l' of the DELL Logo
t.goto(110,-70)
t.setheading(90)
t.pendown()
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()
t.penup()
t.hideturtle()

turtle.d



#Q5. Draw Goku Using Python Turtle

#importing turtle module
import turtle

#setting the background color
turtle.bgcolor('#f0833a')

# Define title of program
turtle.title("Copy Assignment Turtle")

#Create a turtle screen
screen= turtle.Screen()
#Define height and width of screen
screen.setup(1200,600)


goku_hair = turtle.Turtle()
goku_hair.speed(20)
goku_hair.penup()
goku_hair.goto(-270,10)
start=goku_hair.pos()
goku_hair.pendown()
goku_hair.begin_fill()
goku_hair.right(-180)
goku_hair.circle(200,extent=45)
goku_hair.rt(160)
goku_hair.circle(-200,extent=45)
goku_hair.lt(115)
goku_hair.circle(200,extent=45)
goku_hair.rt(160)
goku_hair.circle(-200,extent=60)
goku_hair.rt(205)
goku_hair.circle(200,extent=85)
goku_hair.rt(155)
goku_hair.circle(-200,extent=110)
goku_hair.lt(90)
goku_hair.circle(-50,extent=70)
goku_hair.lt(130)
goku_hair.circle(-200,extent=75)
goku_hair.rt(150)
goku_hair.circle(200,extent=65)
goku_hair.lt(125)
goku_hair.circle(-200,extent=45)
goku_hair.rt(160)
goku_hair.circle(200,extent=45)
goku_hair.lt(80)
goku_hair.circle(-200,extent=35)
goku_hair.rt(160)
goku_hair.circle(200,extent=48)
goku_hair.penup()
goku_hair.goto(-270,10)
goku_hair.pendown()
goku_hair.rt(120)
goku_hair.circle(-200,extent=30)
goku_hair.rt(135)
goku_hair.circle(200,extent=20)
goku_hair.lt(145)
goku_hair.circle(-200,extent=30)
goku_hair.rt(150)
goku_hair.circle(200,extent=25)
goku_hair.lt(165)
goku_hair.circle(-200,extent=30)
goku_hair.rt(120)
goku_hair.circle(-200,extent=15)
goku_hair.lt(120)
goku_hair.circle(200,extent=20)
goku_hair.rt(160)
goku_hair.circle(200,extent=24)

goku_hair.hideturtle()

#Code for drawing right eye of Goku
goku_reye = turtle.Turtle()
goku_reye.speed(20)
goku_reye.penup()
goku_reye.goto(-180,-20)
goku_reye.pendown()
goku_reye.right(125)
goku_reye.forward(5)
e = goku_reye.pos()
goku_reye.rt(90)
goku_reye.begin_fill()
goku_reye.fd(60)
goku_reye.lt(70)
goku_reye.fd(10)
goku_reye.lt(115)
goku_reye.fd(17)
e1 = goku_reye.pos()
goku_reye.fd(40)
goku_reye.goto(e)
goku_reye.end_fill()
goku_reye.goto(e1)
goku_reye.color("black","white")
goku_reye.begin_fill()
goku_reye.rt(70)
goku_reye.fd(17)
goku_reye.lt(85)
goku_reye.fd(37)
goku_reye.end_fill()
goku_reye.begin_fill()
goku_reye.color("black")
goku_reye.circle(5)
goku_reye.end_fill()
goku_reye.hideturtle()

#Code for drawing left eye of Goku
goku_leye = turtle.Turtle()
goku_leye.speed(20)
goku_leye.penup()
goku_leye.goto(-150,-20)
goku_leye.pendown()
goku_leye.left(125)
goku_leye.backward(5)
e = goku_leye.pos()
goku_leye.lt(90)
goku_leye.begin_fill()
goku_leye.bk(60)
goku_leye.rt(70)
goku_leye.bk(10)
goku_leye.rt(115)
goku_leye.bk(17)
e1 = goku_leye.pos()
goku_leye.bk(40)
goku_leye.goto(e)
goku_leye.end_fill()
goku_leye.goto(e1)
goku_leye.color("black","white")
goku_leye.begin_fill()
goku_leye.lt(70)
goku_leye.bk(17)
goku_leye.rt(85)
goku_leye.bk(37)
goku_leye.end_fill()
goku_leye.begin_fill()
goku_leye.color("black")
goku_leye.circle(5)
goku_leye.end_fill()
goku_leye.hideturtle()


#face of goku
goku_face = turtle.Turtle()
goku_face.speed(20)
goku_face.penup()
goku_face.goto(-270,10)
goku_face.pendown()
goku_face.rt(65)
goku_face.fd(100)
goku_face.left(30)
goku_face.fd(80)
goku_face.lt(70)
goku_face.fd(80)
goku_face.left(30)
goku_face.fd(109)
goku_face.hideturtle()

#code for nose of goku
goku_nose = turtle.Turtle()
goku_nose.speed(20)
goku_nose.penup()
goku_nose.goto(-165,-50)
goku_nose.pendown()
goku_nose.right(90)
goku_nose.fd(15)
goku_nose.hideturtle()

#Code for smile of goku
goku_smile=turtle.Turtle()
goku_smile.speed(20)
goku_smile.penup()
goku_smile.goto(-185,-75)
goku_smile.pendown()
goku_smile.rt(55)
goku_smile.fd(10)
goku_smile.lt(60)
goku_smile.fd(30)
goku_smile.lt(60)
goku_smile.fd(10)
goku_smile.penup()
goku_smile.goto(-170,-90)
goku_smile.pendown()
goku_smile.rt(60)
goku_smile.fd(15)
goku_smile.hideturtle()

#code for the sword

#go to starting position
goku_sword = turtle.Turtle()
goku_sword.speed(20)
goku_sword.penup()
goku_sword.goto(270,-80)
goku_sword.right(90)
goku_sword.forward(150)
goku_sword.right(90)
goku_sword.forward(130)

#end of handle
goku_sword.pendown()
goku_sword.right(90)
goku_sword.forward(50)
goku_sword.right(90)
goku_sword.forward(50)
goku_sword.right(90)
goku_sword.forward(50)
goku_sword.right(90)
goku_sword.forward(50)
goku_sword.end_fill()

#right handle
goku_sword.right(180)
goku_sword.forward(50)
goku_sword.left(90)
goku_sword.forward(15)
goku_sword.right(45)
goku_sword.forward(75)
goku_sword.right(90)
goku_sword.forward(50)
goku_sword.left(45)
goku_sword.forward(75)
goku_sword.left(135)
goku_sword.forward(75)

#right blade
goku_sword.right(90)
goku_sword.forward(200)
goku_sword.left(45)
goku_sword.forward(75)

#left blade
goku_sword.left(90)
goku_sword.forward(75)
goku_sword.left(45)
goku_sword.forward(200)


#left handle
goku_sword.right(90)
goku_sword.forward(75)
goku_sword.left(135)
goku_sword.forward(75)
goku_sword.left(45)
goku_sword.forward(50)
goku_sword.right(90)
goku_sword.forward(75)

#decoration on end of handle
goku_sword.left(45)
goku_sword.penup()
goku_sword.forward(12)
goku_sword.right(90)
goku_sword.forward(3)
goku_sword.left(90)
goku_sword.pendown()
goku_sword.begin_fill()
goku_sword.fillcolor("#fcc201")
goku_sword.forward(25)
goku_sword.left(90)
goku_sword.forward(25)
goku_sword.left(90)
goku_sword.forward(25)
goku_sword.left(90)
goku_sword.forward(25)
goku_sword.left(90)
goku_sword.left(135)
goku_sword.end_fill()
#left decoration on handle

goku_sword.penup()
goku_sword.forward(100)
goku_sword.left(90)
goku_sword.forward(10)
goku_sword.pendown()
goku_sword.begin_fill()
goku_sword.fillcolor("red")
goku_sword.forward(45)
goku_sword.right(45)
goku_sword.forward(35)
goku_sword.right(135)
goku_sword.forward(45)
goku_sword.right(45)
goku_sword.forward(35)
goku_sword.end_fill()

#right decoration on handle
goku_sword.left(45)
goku_sword.penup()
goku_sword.forward(50)
goku_sword.pendown()
goku_sword.begin_fill()
goku_sword.fillcolor("red")
goku_sword.forward(45)
goku_sword.left(45)
goku_sword.forward(35)
goku_sword.left(135)
goku_sword.forward(45)
goku_sword.left(45)
goku_sword.forward(35)
goku_sword.end_fill()
goku_sword.penup()

#beginning of blade decoration
goku_sword.right(45)
goku_sword.forward(22)
goku_sword.right(90)

#blade decoration
goku_sword.pendown()

goku_sword.right(45)
goku_sword.forward(55)
goku_sword.left(45)
goku_sword.forward(195)
goku_sword.left(45)
goku_sword.forward(55)
goku_sword.left(90)
goku_sword.forward(55)
goku_sword.left(45)
goku_sword.forward(195)
goku_sword.left(45)
goku_sword.forward(55)
goku_sword.right(45)
goku_sword.penup()

#blade decoration 2
goku_sword.right(180)
goku_sword.forward(20)
goku_sword.pendown()
goku_sword.begin_fill()
goku_sword.fillcolor("#fcc201")
goku_sword.right(45)
goku_sword.forward(35)
goku_sword.left(45)
goku_sword.forward(185)
goku_sword.left(45)
goku_sword.forward(35)
goku_sword.left(90)
goku_sword.forward(35)
goku_sword.left(45)
goku_sword.forward(185)
goku_sword.left(45)
goku_sword.forward(35)
goku_sword.end_fill()
goku_sword.penup()
goku_sword.right(45)

#handle decoration middle
goku_sword.forward(35)
goku_sword.pendown()
goku_sword.begin_fill()
goku_sword.fillcolor("blue")
goku_sword.right(45)
goku_sword.forward(15)
goku_sword.left(45)
goku_sword.forward(35)
goku_sword.left(135)
goku_sword.forward(16)
goku_sword.right(90)
goku_sword.forward(16)
goku_sword.left(135)
goku_sword.forward(35)
goku_sword.left(45)
goku_sword.forward(15)
goku_sword.end_fill()
goku_sword.penup()
goku_sword.hideturtle()


#code for writing dragon ball z
def write(message,pos):
        x,y=pos
        # Define color of the text
        turtle.pencolor("yellow")
        turtle.penup()
        turtle.goto(x,y)
        # Defining font style and size
        style=('Verdana',30,'bold')
        turtle.write(message,font=style)

write('Dragon',(-330,-200))

def write(message,pos):
        x,y=pos
        # Define color of the text
        turtle.pencolor("red")
        turtle.penup()
        turtle.goto(x,y)
        # Defining font style and size
        style=('Verdana',30,'bold')
        turtle.write(message,font=style)

write('Ball',(-160,-200))

def write(message,pos):
        x,y=pos
        # Define color of the text
        turtle.pencolor("red")
        turtle.penup()
        turtle.goto(x,y)
        # Defining font style and size
        style=('Verdana',40,'bold')
        turtle.write(message,font=style)

write('Z',(-70,-205))

def write(message,pos):
        x,y=pos
        # Define color of the text
        turtle.pencolor("blue")
        turtle.penup()
        turtle.goto(x,y)
        # Defining font style and size
        style=('Verdana',15)
        turtle.write(message,font=style)

write('The Legacy of Goku',(-300,-240))
turtle.hideturtle()

#code for holding screen 
turtle.mainloop()







#new items 15 dec 2022
#format shape

import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
h = 0
def draw(ang,n):
    t.circle(5+n,60)
    t.left(ang)
    t.circle(5+n,60)
t.pensize(5)
t.goto(0,0)
for i in range(250):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    t.pencolor(c)
    t.fillcolor('black')
    t.begin_fill()
    draw(90,i*0.05)
    draw(160,i*1.2)
    t.end_fill()
    t.up()
    draw(180,i)
    draw(90,i*2)
    t.down()
t.done()'''





#new items 15 dec 2022
#graphic Design

import turtle as t
import colorsys
t.bgcolor('black')
t.pensize(2)
t.speed(500000)
h=0.4
t.up()
t.goto(0,100)
t.down()
for i in range(260):
    c=colorsys.hsv_to_rgb(h,1,1)
    h +=0.002
    t.color(c)
    t.up()
    t.fd(i*2)
    t.down()
    t.circle(i,-150)
    t.fd(i)
    t.circle(i,-150)
t.done()



#new items 15 dec 2022
#graphic Design

import turtle as t
import colorsys
t.bgcolor('black')
t.pensize(2)
t.speed(500000)
h=0.4
t.up()
t.goto(0,100)
t.down()
for i in range(260):
    c=colorsys.hsv_to_rgb(h,1,1)
    h +=0.002
    t.color(c)
    t.up()
    t.fd(i*2)
    t.down()
    t.circle(i,-100)
    t.fd(i)
    t.circle(i,-100)
t.done()



#Graphic picture of virus

import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 0  
b = 0  
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True): 
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break;
  
