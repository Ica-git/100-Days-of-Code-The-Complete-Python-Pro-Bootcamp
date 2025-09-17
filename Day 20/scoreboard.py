from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")
END_FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=END_FONT)
