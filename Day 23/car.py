import random
from turtle import Turtle


car_colors = ["lightblue", "lightgreen", "lightpink", "lightskyblue", "lightgoldenrod", "lightcyan", "lightcoral", "lightseagreen", "lightsteelblue", "lightyellow", "lavender", "powderblue", "peachpuff", "mistyrose", "palegreen", "paleturquoise", "papayawhip", "thistle", "honeydew", "mintcream"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(car_colors))
        self.penup()
        self.spawn()

    def spawn(self):
        y_cor = random.randint(-255, 270)
        self.teleport(320, y_cor)
        self.setheading(180)

    def car_move(self):
        if self.xcor() < -300:
            self.hideturtle()
        self.forward(10)


