import time
from turtle import Screen
import snake
import food
from scoreboard import Scoreboard

""" Reading a file
with open(score.txt) as file: #this is a method to manage the file automatically - THING automated.
    contents = file.read()
    print(contents)
    
scorestore = open(score.txt)
contents = scorestore.read()
print(contents)
scorestore.close() #it's important to close to free up the resources
"""
""" Writing a file
with open(score.txt, mode="a") as file: #modes r = read w = write a = append
    file.write("New text.")
    file.write("\nNew text.")
    
If there is no file in such a name we can create file with the open("name for file", mode = "w").
"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0, 0, 0)
screen.title("Snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

is_snake_alive = True
while is_snake_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        if snake.head.distance(food) < 15:
            new_food = True
            while new_food:
                food.refresh()
                for segment in snake.segments:
                    if food.distance(segment) >= 15:
                        new_food = False
                        break
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset()

     #Detect collision with tail
    snake_body = snake.segments[1:]
    for body in snake_body:
        if snake.head.distance(body) < 10:
            scoreboard.reset_scoreboard()
            snake.reset()


#screen.exitonclick()
