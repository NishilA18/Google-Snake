# Google Snake

A Python implementation of the classic Google Snake game with a modern, minimalist design inspired by Google's style.

## Features

- 🐍 Classic Snake gameplay with smooth controls
- 🎮 Google-inspired color scheme (Green snake, Red food)
- 📊 Score tracking
- 🔄 Restart functionality
- 🎯 Smooth animations at 10 FPS

## Requirements

- Python 3.7+
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NishilA18/Google-Snake.git
cd Google-Snake
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

Run the game:
```bash
python snake_game.py
```

### Controls

- **Arrow Keys**: Move the snake (UP, DOWN, LEFT, RIGHT)
- **SPACE**: Restart the game when Game Over

### Game Rules

1. Guide the snake to eat the red food
2. Each food consumed adds 10 points to your score
3. The snake grows with each food eaten
4. Avoid hitting the walls or the snake's own body
5. Game Over occurs when you collide with a wall or yourself

## Game Features

- **Snake**: Green colored snake that grows as it eats food
- **Food**: Red squares that the snake must eat to grow and score points
- **Score**: Displayed in the top-left corner
- **Difficulty**: Fixed at 10 moves per second (adjustable in code)

## Customization

You can customize the game by modifying constants in `snake_game.py`:

```python
SCREEN_WIDTH = 800        # Game window width
SCREEN_HEIGHT = 600       # Game window height
GRID_SIZE = 20            # Size of each grid cell
FPS = 10                  # Moves per second (higher = faster)
```

## Color Scheme

- Background: Dark Gray `#282828`
- Snake: Google Green `#4CAF50`
- Food: Google Red `#F44336`
- Text: White `#FFFFFF`
- Game Over: Google Yellow `#FFC107`

## Future Enhancements

- [ ] Difficulty levels
- [ ] High score tracking
- [ ] Sound effects
- [ ] Power-ups
- [ ] Different game modes
- [ ] Leaderboard

## License

This project is open source and available under the MIT License.

## Author

Created by NishilA18