###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as t
import random



# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

def one_line():
    tim.dot(30, random.choice(color_list))
    for i in range(9):
        tim.forward(50)
        tim.dot(30, random.choice(color_list))

def next_line_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def next_line_right():
    tim.right(90)
    tim.forward(50)
    tim.right(90)





color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = t.Turtle()

tim.shape("turtle")
tim.color("DarkGreen")
t.colormode(255)
tim.penup()
tim.speed(120)

# for i in range(10):
#     one_line()
#     if i % 2 == 0:
#         next_line_left()
#     else:
#         next_line_right()



start_y = -200
for i in range(10):
    tim.teleport(-250, start_y)
    one_line()
    start_y = start_y + 50






screen = t.Screen()
screen.exitonclick()