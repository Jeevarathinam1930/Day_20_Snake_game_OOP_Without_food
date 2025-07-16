from turtle import Turtle
position=[(0,0),(-20,0),(-40,0)]
move_distance=20
LEFT=180
RIGHT=0
UP=90
DOWN=270
class Snake:
    def __init__(self):
        self.moving_segment = []
        self.create_snake()
        self.head=self.moving_segment[0]


    def create_snake(self):
        for i in position:
            tim=Turtle()
            tim.penup()
            tim.color("white")
            tim.shape("square")
            tim.goto(i)
            self.moving_segment.append(tim)

    def move(self):
        for moving in range(len(self.moving_segment)-1, 0, -1):
            new_x = self.moving_segment[moving - 1].xcor()
            new_y = self.moving_segment[moving - 1].ycor()
            self.moving_segment[moving].goto(x=new_x, y=new_y)
        self.head.forward(move_distance)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
