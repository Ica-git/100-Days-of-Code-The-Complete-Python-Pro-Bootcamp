from turtle import Turtle

MOVE_DISTANCE = 20

class Chick(Turtle):
    def __init__(self):
        super().__init__()
        self.game_speed = 0.1
        self.shape("turtle")
        self.color("yellow")
        self.setheading(90)
        self.penup()
        self.to_start()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def to_start(self):
        self.teleport(0, -280)

    def car_speed_up(self):
        self.game_speed *= 0.8
