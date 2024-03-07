import random
from turtle import Turtle

import score


class Food():

    def __init__(self):
        self.food = Turtle("circle")
        self.food.hideturtle()
        self.food.penup()
        self.food.shapesize(0.75, 0.75, 0.75)


    def random_food(self):
        random_x = random.randint(-450, 450)
        random_y = random.randint(-350, 350)
        self.food.goto(random_x, random_y)
        self.food.color("white")
        self.food.showturtle()

    def get_x_y(self):
        return self.food.xcor(),self.food.ycor()

    def eat_food(self, snake,head):
        if head.distance(self.get_x_y()) < 20:
            self.random_food()
            snake.increase_body()
            return True