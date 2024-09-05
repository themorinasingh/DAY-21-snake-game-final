from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("black")
        self.penup()
        # self.shapesize(stretch_wid =.8, stretch_len = .8)
        self.refresh()

    def refresh(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x,y)



