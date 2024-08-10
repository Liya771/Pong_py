from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, postion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(postion)

    def forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def backward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)