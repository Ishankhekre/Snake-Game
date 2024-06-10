from snake import Snake
from turtle import Turtle, Screen
from score_board import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
  
  
  
  
  
  
