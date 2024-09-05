from turtle import Screen
from snake import Snake
import time
from food import Food
from ScoreBoard import Score
screen = Screen()
screen.bgcolor("yellow")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake(color="black")
food = Food()

score_tracker = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    time.sleep(.15)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.add_length()
        food.refresh()
        score_tracker.update_score_board()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_tracker.game_over()

    for serpant in snake.my_snake[1:]:
        if snake.head.distance(serpant) < 10:
            game_is_on = False
            score_tracker.game_over()




screen.exitonclick()