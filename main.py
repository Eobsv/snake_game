import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0,0,0)
screen.title("Snake game")

starting_pos = [(0, 0,), (-20, 0,), (-40, 0)]
snake = []
for pos in starting_pos:
    segment_new = turtle.Turtle("square")
    segment_new.color("white")
    segment_new.penup()
    segment_new.goto(pos)
    snake.append(segment_new)

is_snake_alive = True

while is_snake_alive:
    for seg in snake:
        seg.forward(20)


screen.exitonclick()
