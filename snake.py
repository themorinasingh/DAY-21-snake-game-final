from turtle import Turtle

positions = [(0,0), (-20, 0), (-40, 0)]
Distance = 20
#setting up dicrections

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self, color="white"):
        self.my_snake = []
        self.color = color
        self.snake_maker()
        self.head = self.my_snake[0]


    def snake_maker(self):
        for position in positions:
            new_part = Turtle(shape="square")
            new_part.color(self.color)
            new_part.penup()
            new_part.goto(position)
            self.my_snake.append(new_part)

    def move(self):
        for i in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[i -1].xcor()
            new_y = self.my_snake[i -1].ycor()
            self.my_snake[i].goto(new_x, new_y)

        self.head.forward(Distance)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def add_length(self):
        new_part = Turtle(shape="square")
        new_part.color(self.color)
        new_part.penup()
        self.my_snake.append(new_part)


