from turtle import Screen
from snake import Snake
import time as t
screen=Screen()
snake=Snake()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
looping=True
while looping==True:
    screen.update()
    t.sleep(0.1)
    snake.move()
screen.exitonclick()