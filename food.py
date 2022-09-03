import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("blue")
        random_x = random.randint(-27, 27)
        random_y = random.randint(-27, 27)
        self.goto(random_x * 10, random_y * 10)

    def refresh(self):
        random_x = random.randint(-27, 27)
        random_y = random.randint(-27, 27)
        self.goto(random_x * 10, random_y * 10)
