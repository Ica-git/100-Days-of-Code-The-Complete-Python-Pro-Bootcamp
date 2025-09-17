from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 60, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


        self.line()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


    def line(self):
        self.teleport(0, 300)
        self.shape("square")
        self.pendown()
        self.shapesize(0.5)
        self.penup()




        self.goto(0, -300)

    # def update_scoreboard_r(self):
    #     self.clear()