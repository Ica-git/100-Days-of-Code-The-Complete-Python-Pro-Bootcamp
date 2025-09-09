import turtle as t
import random
import matplotlib.colors as mcolors

tim = t.Turtle()

tim.shape("turtle")
tim.color("DarkGreen")
t.colormode(255)

# for i in range(4):
#     tim.right(90)
#     tim.forward(100)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for i in range(3,11):
#     tim.pencolor(random.choice(all_colors))
#     angel = 360 / i
#     for j in range(0,i):
#         tim.forward(100)
#         tim.right(angel)
# tim.forward(100)

# def random_color(colors):
#     tim.pencolor(random.choice(colors))

# all_colors = [
#     "red", "blue", "green", "yellow", "orange", "purple",
#     "pink", "brown", "black", "gray", "cyan", "magenta",
#     "gold", "silver", "lime", "indigo", "violet", "navy",
#     "turquoise", "teal", "maroon", "coral", "salmon", "khaki",
#     "plum", "orchid", "beige", "chocolate", "tan", "olive"
# ]

# def random_turn(directions):
#     tim.setheading(random.choice(directions))
#
#
# directions = [0,90,180,270]
#
# tim.pensize(10)
# tim.speed(10)
#
# for i in range(200):
#     random_turn(directions)
#     random_color()
#     tim.forward(30)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)

tim.speed(120)

tim.circle(100)

times = 75

for i in range(times):
    angel = 360/times
    random_color()
    tim.left(angel)
    tim.circle(100)











screen = t.Screen()
screen.exitonclick()


