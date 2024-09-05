from turtle import Turtle

#setting up constants
FONT = ("ariel", 25, "normal")
ALIGN = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0,270)
        self.write_score()

    def write_score(self):
        self.write(arg = "SCORE: " + str(self.score), move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)


    def update_score_board(self):
        self.clear()
        self.score += 1
        self.write_score()
