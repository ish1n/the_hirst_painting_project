import colorgram
import turtle
from turtle import Screen
import random

screen = Screen()
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
num_of_dots=100
# rgb_colors=[]
# colors = colorgram.extract('python_project.jpeg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors=(r , g , b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
tim.setheading(225)
tim.fd(250)
tim.setheading(0)
num_of_dots=100
color_list = [(242, 225, 204), (202, 154, 115), (244, 218, 232), (215, 239, 226), (213, 225, 240), (134, 163, 186), (142, 92, 60), (195, 140, 160), (67, 104, 132), (135, 176, 155), (136, 74, 98), (65, 117, 92), (221, 201, 135), (189, 92, 115), (204, 94, 73), (232, 166, 185), (159, 146, 63), (22, 39, 66), (84, 155, 122), (238, 170, 158), (161, 210, 187), (54, 34, 18), (60, 26, 46), (19, 45, 31), (107, 118, 166), (112, 37, 63), (179, 183, 219), (42, 53, 108), (69, 153, 168), (24, 91, 65)]
for i in range(1,num_of_dots+1) :

    tim.dot(20,random.choice(color_list))
    tim.fd(50)
    if i % 10 == 0 :
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)
#i.color(random.choice(color_list))
tim.ht()
screen.exitonclick()
