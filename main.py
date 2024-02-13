from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



game_is_on = True
screen = Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment in the tail:
        # trigger scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

        


screen.exitonclick()



