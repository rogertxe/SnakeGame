from turtle import Screen
import snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Feed the snake")
screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()











screen.exitonclick()