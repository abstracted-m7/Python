from turtle import *
import turtle as turtle_module
import random

# penup or pu means pick pen up & .color means turtle color

t_red = Turtle(shape="turtle")
t_red.color("red")
t_red.penup() 

t_blue = Turtle(shape="turtle")
t_blue.color("blue")
t_blue.penup()

t_green = Turtle(shape="turtle")
t_green.color("green")
t_green.penup()

t_yellow = Turtle(shape="turtle")
t_yellow.color("yellow")
t_yellow.penup()

t_pink = Turtle(shape="turtle")
t_pink.color("pink")
t_pink.penup()

screen = Screen()
exit = turtle_module.Screen()
screen.setup(width=500,height=400)

# user_bet means input which color we pick for the match

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race. Enter the color")

# Apply .goto function for tartle position

t_blue.goto(-450,-300)
t_yellow.goto(-450,-150)
t_red.goto(-450,0)
t_pink.goto(-450,150)
t_green.goto(-450,300)

if user_bet:
    race_is_on = True

while race_is_on:

    for i in t_blue,t_yellow,t_red,t_pink,t_green:
        #apply Xcor function
        if i.xcor()>470:
            race_is_on=False
            winner=i.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is winner")
            else:
                print(f"You've lose! The {winner} turtle is winner")

        #using randit function. This method is an alias for randrange(start, stop+1)
        rand_distance=random.randint(0,10)
        #using forward function.
        #The turtle.forward() method is used to move the turtle forward by the value of the argument that it takes. 
        i.forward(rand_distance)
    
#using exitonclick function for screen of. 
exit.exitonclick()
