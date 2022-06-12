import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)
color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]


turtle_size =20
tim = Turtle()
screen = Screen()
tim.shape('turtle')


tim.penup()
turtle_height_addition = 0

for column in range(10):

    tim.goto(turtle_size - screen.window_width()/2, - screen.window_height()/2 + turtle_size + turtle_height_addition)
    turtle_height_addition += 50
    for row in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

turtle.exitonclick()









