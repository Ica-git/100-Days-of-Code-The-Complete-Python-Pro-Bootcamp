from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")
END_FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())


    # def game_over(self):
    #     self.penup()
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=END_FONT)
