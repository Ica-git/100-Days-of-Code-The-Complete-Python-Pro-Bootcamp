from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        next_x = self.xcor() + self.x_move
        next_y = self.ycor() + self.y_move
        self.goto(next_x, next_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.teleport(0,0)
        self.move_speed = 0.1
        self.bounce_x()
