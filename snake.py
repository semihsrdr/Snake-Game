from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
class Snake():

    def __init__(self):
        self.bodies=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_body=Turtle("square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(position)
            self.bodies.append(new_body)



    def move_snake(self):


        for body_num in range(len(self.bodies)-1,0,-1):
            new_x=self.bodies[body_num-1].xcor()
            new_y=self.bodies[body_num-1].ycor()
            self.bodies[body_num].goto(new_x,new_y)

        self.bodies[0].forward(DISTANCE)

        if self.bodies[0].xcor()>500:
            self.bodies[0].setx(-500)
        elif self.bodies[0].xcor()<-500:
            self.bodies[0].setx(500)
        elif self.bodies[0].ycor()>400:
            self.bodies[0].sety(-400)
        elif self.bodies[0].ycor()<-400:
            self.bodies[0].sety(400)


    def turn_left(self):
        self.bodies[0].setheading(self.bodies[0].heading()+90)
    def turn_right(self):
        self.bodies[0].setheading(self.bodies[0].heading()-90)

    def increase_body(self):
        new_body = Turtle("square")
        new_body.color("black")
        new_body.hideturtle()
        new_body.penup()
        new_body.goto(self.bodies[-1].position())  # Yeni parçayı yılanın son parçasının konumuna taşı
        self.bodies.append(new_body)
        new_body.color("white")
        new_body.showturtle()

    def is_alive(self):
        for i in self.bodies[:1:-1]:
            if self.bodies[0].distance(i)<10:
                print("game over")
                return False




