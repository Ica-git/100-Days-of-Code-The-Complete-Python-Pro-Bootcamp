import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(*position)
        self.color("white")

    def go_up(self):
        new_y = self.ycor()
        if new_y < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()
        if new_y > - 240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


