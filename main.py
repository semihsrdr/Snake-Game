
import time
from turtle import Screen

import score
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right,"Right")


game_on=True
food.random_food()
while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move_snake()
    if food.eat_food(snake,snake.bodies[0]):
        score.increase_score()
    if snake.is_alive()==False:
        for i in range(3):
            screen.bgcolor("red")
            time.sleep(0.3)
            screen.bgcolor("black")
            time.sleep(0.3)

        game_on==False
        score.finish_game()
        break

screen.exitonclick()



