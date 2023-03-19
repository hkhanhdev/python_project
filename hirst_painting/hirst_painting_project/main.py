###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r,g,b))
# print(rgb_colors)
import random

colors_list = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
import turtle
turtle.colormode(255) # change color mode to rgb mode
tim = turtle.Turtle() # create new object
tim.speed('fastest') # change turtle speed
tim.penup() #remove the pen line
tim.hideturtle()   # hide the turtle so that we can only see dots
tim.setheading(225) # set turtle direction
tim.forward(300) #move forward
tim.setheading(0) #now set direction to old direction
number_of_dots = 100



for dot in range(1,number_of_dots+1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




turtle.exitonclick()