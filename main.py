import time
from turtle import Screen
import snake
import food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0, 0, 0)
screen.title("Snake game")
screen.tracer(0)

snake_in_game = snake.Snake()
food = food.Food()
is_snake_alive = True

screen.listen()
screen.onkey(snake_in_game.up, "Up")
screen.onkey(snake_in_game.down, "Down")
screen.onkey(snake_in_game.left, "Left")
screen.onkey(snake_in_game.right, "Right")

while is_snake_alive:
    screen.update()
    time.sleep(0.1)

    snake_in_game.move()
    if snake_in_game.head.distance(food) < 15:
        food.refresh()
        snake_in_game.snake_ate_food()

screen.exitonclick()
