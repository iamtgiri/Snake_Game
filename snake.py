from turtle import *
from random import randrange
from freegames import square, vector

# Initialize the game screen
title("Snake Game")
bgcolor("forestgreen")
score = 0
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Initialize game state
def change(x, y):
    """Change the direction of the snake."""
    aim.x = x
    aim.y = y

def inside(head):
    """Check if the head is within the game boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move the snake forward and update game state."""
    global score
    head = snake[-1].copy()
    head += aim

    # Check if snake has hit the wall or itself
    if not inside(head) or head in snake:
        game_over()
        return

    snake.append(head)

    # Check if the snake ate the food
    if head.x == food.x and head.y == food.y:
        score += 1
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Clear previous game frame and draw the new one
    clear()

    # Draw snake
    for body in snake:
        square(body.x, body.y, 9, 'yellow')

    # Draw food
    square(food.x, food.y, 9, 'white')

    # Display score
    display_score()

    update()
    ontimer(move, 100)

def game_over():
    """Display game over message and reset game."""
    clear()
    square(0, 0, 9, 'red')  # Show red square where the head collided
    update()
    goto(0, 0)
    color("white")
    write(f"Game Over! Score: {score}", align="center", font=("Arial", 16, "bold"))
    ontimer(reset_game, 3000)  # Reset game after 3 seconds

def reset_game():
    """Reset the game state."""
    global score, snake, food, aim
    score = 0
    snake = [vector(10, 0)]
    food = vector(0, 0)
    aim = vector(0, -10)
    clear()
    move()

def display_score():
    """Display the current score on the screen."""
    penup()
    goto(-180, 180)
    color("white")
    write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
    pendown()

# Game setup
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')  # Move Right
onkey(lambda: change(-10, 0), 'Left')  # Move Left
onkey(lambda: change(0, 10), 'Up')    # Move Up
onkey(lambda: change(0, -10), 'Down') # Move Down

# Start the game
move()
done()
