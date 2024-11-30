
# Snake Game

This is a simple implementation of the classic Snake game built using Python's `turtle` graphics library. The game features real-time movement of a snake that grows longer as it eats food. The player must navigate the snake, avoid collisions with the walls or itself, and try to achieve the highest score.

## Features

- **Game Mechanics**: The snake moves on the screen, and the player controls its direction using the arrow keys. The snake grows longer each time it eats food.
- **Game Over Logic**: The game ends if the snake collides with the walls or itself. Upon game over, the player's score is displayed.
- **Score Tracking**: The current score is displayed at the top left of the screen, increasing with each piece of food eaten.
- **Game Reset**: After a game over, the game resets automatically after a brief pause.
  
## Requirements

- Python 3.x
- `turtle` graphics library (comes pre-installed with Python)

## How to Play

1. Run the Python script to start the game.
2. Use the arrow keys to control the direction of the snake:
   - **Up**: Move up
   - **Down**: Move down
   - **Left**: Move left
   - **Right**: Move right
3. Try to eat the white food squares to grow the snake.
4. Avoid hitting the walls or colliding with the snake's own body.
5. The game will display a "Game Over" message when the snake hits a wall or itself, and the score will be shown.
6. After the game over, the game will reset automatically.

## Code Structure

- **`change(x, y)`**: Updates the direction of the snake.
- **`inside(head)`**: Checks if the snake's head is within the screen boundaries.
- **`move()`**: Controls the movement of the snake, food generation, collision detection, and updates the game state.
- **`game_over()`**: Displays a "Game Over" message and resets the game.
- **`reset_game()`**: Resets the game state and starts a new round.
- **`display_score()`**: Displays the current score on the screen.

## Installation

1. Ensure that Python 3 is installed on your system.
2. No additional libraries are required as the `turtle` graphics module comes pre-installed with Python.
3. Save the code to a `.py` file, for example `snake.py`.
4. Run the Python file in your terminal or IDE.

```bash
python snake_game.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
