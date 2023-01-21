from turtle import Turtle, Screen
import turtle as t
from random import *
import random
tim=t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("medium orchid")
# make square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# dashes
# for a in range(0,10):
#     tim.forward(10)
#
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()




# random color snakes
def ran_color():

    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col=(r,g,b)
    return col

# directions=[0,90,180,270]
# for _ in range(200):
#     tim.color(ran_color())
#     tim.pensize(15)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


## make spirograph
for _ in range(100):
    tim.color(ran_color())

    tim.circle(50)
    tim.left(5)


# diff shapes
# def draw_shape(num_of_side):
#     shapes = 360 / num_of_side
#     for _ in range(num_of_side):
#
#         tim.forward(100)
#         tim.right(shapes)
# for i in range(3,10):
#     tim.color(random.choice(colours))
#
#     draw_shape(i)
#

screen=Screen()
screen.exitonclick()