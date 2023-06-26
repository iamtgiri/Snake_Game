from turtle import *
from random import randrange
from freegames import square, vector

# Set up the game area
border = Turtle(visible=False)
border.speed(0)
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(6)
border.pencolor("white")
for _ in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -1)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -290 <= head.x <= 290 and -290 <= head.y <= 290

def move():
    head = snake[-1].copy()
    head += aim

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('snake', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'yellow')

    # Draw a circle for the food instead of a square
    penup()
    goto(food.x, food.y)
    pendown()
    color('white')
    begin_fill()
    circle(3)
    end_fill()

    update()
    ontimer(move, 5)

# Set up the screen
setup(600, 600)
title("Snake Game")
bgcolor("forestgreen")  # Set the background color to green

# Set up the game area
border = Turtle(visible=False)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(1, 0), 'Right')
onkey(lambda: change(-1, 0), 'Left')
onkey(lambda: change(0, 1), 'Up')
onkey(lambda: change(0, -1), 'Down')

move()
done()
