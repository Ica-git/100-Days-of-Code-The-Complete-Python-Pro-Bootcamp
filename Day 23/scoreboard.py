from turtle import Turtle
from art import logo
ALIGMENT = "center"
FONT = ("Courier", 24, "bold")
END_FONT = ("Courier", 11, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.teleport(-200,260)
        self.write(f"Level: {self.level}", align=ALIGMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.teleport(0,-100)
        self.write(logo, align=ALIGMENT, font=END_FONT)
        self.teleport(0, -120)
        self.write(f"Level: {self.level}", align=ALIGMENT, font=FONT)