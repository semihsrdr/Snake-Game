from turtle import Turtle

class Score():
    score=0
    text_turtle = Turtle()
    text_turtle.hideturtle()


    def __init__(self):
        self.text_turtle.color("white")
        self.text_turtle.penup()
        self.text_turtle.goto(0, 350)
        self.text_turtle.write("Score : "+str(self.score), align="center", font=("Arial", 20, "bold"))
    def increase_score(self):
        self.text_turtle.clear()
        self.score+=1
        self.text_turtle.write("Score : "+str(self.score), align="center", font=("Arial", 20, "bold"))
    def finish_game(self):

        self.text_turtle.goto(0, 0)
        self.text_turtle.write("Game Over", align="center", font=("Arial", 60, "bold"))

