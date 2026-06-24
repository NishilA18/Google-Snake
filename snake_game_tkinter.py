import tkinter as tk
import random
from collections import deque

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Snake")
        self.root.resizable(False, False)
        
        # Game constants
        self.GRID_SIZE = 20
        self.GRID_WIDTH = 40
        self.GRID_HEIGHT = 30
        self.CANVAS_WIDTH = self.GRID_WIDTH * self.GRID_SIZE
        self.CANVAS_HEIGHT = self.GRID_HEIGHT * self.GRID_SIZE
        
        # Colors
        self.BG_COLOR = "#282828"
        self.SNAKE_COLOR = "#4CAF50"
        self.SNAKE_HEAD_COLOR = "#90EE90"
        self.FOOD_COLOR = "#F44336"
        self.TEXT_COLOR = "white"
        
        # Create canvas
        self.canvas = tk.Canvas(
            root,
            width=self.CANVAS_WIDTH,
            height=self.CANVAS_HEIGHT,
            bg=self.BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(pady=10)
        self.canvas.focus()
        
        # Bind keys to root window for better capture
        self.root.bind("<Up>", self.on_key_press)
        self.root.bind("<Down>", self.on_key_press)
        self.root.bind("<Left>", self.on_key_press)
        self.root.bind("<Right>", self.on_key_press)
        self.root.bind("<space>", self.on_key_press)
        
        # Score label
        self.score_label = tk.Label(root, text="Score: 0", fg=self.TEXT_COLOR, bg="#1a1a1a", font=("Arial", 16))
        self.score_label.pack()
        
        # Game over label
        self.game_over_label = tk.Label(root, text="", fg="#FFC107", bg="#1a1a1a", font=("Arial", 20, "bold"))
        self.game_over_label.pack()
        
        # Instructions label
        self.instruction_label = tk.Label(root, text="Use Arrow Keys to move | Press SPACE to restart", fg="#999999", bg="#1a1a1a", font=("Arial", 10))
        self.instruction_label.pack()
        
        # Initialize game state
        self.reset_game()
    
    def reset_game(self):
        """Initialize or reset the game state"""
        self.snake = deque([
            (self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2),
            (self.GRID_WIDTH // 2 - 1, self.GRID_HEIGHT // 2),
            (self.GRID_WIDTH // 2 - 2, self.GRID_HEIGHT // 2)
        ])
        self.direction = (1, 0)  # Moving right
        self.next_direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        self.game_over_label.config(text="")
        self.update_score_display()
        self.game_loop()
    
    def spawn_food(self):
        """Spawn food at a random location"""
        while True:
            food = (random.randint(0, self.GRID_WIDTH - 1), 
                   random.randint(0, self.GRID_HEIGHT - 1))
            if food not in self.snake:
                return food
    
    def on_key_press(self, event):
        """Handle key press events"""
        key = event.keysym
        
        if self.game_over and key == "space":
            self.reset_game()
            return
        
        # Direction mappings
        if key == "Up" and self.direction != (0, 1):
            self.next_direction = (0, -1)
        elif key == "Down" and self.direction != (0, -1):
            self.next_direction = (0, 1)
        elif key == "Left" and self.direction != (1, 0):
            self.next_direction = (-1, 0)
        elif key == "Right" and self.direction != (-1, 0):
            self.next_direction = (1, 0)
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.game_over = True
            self.game_over_label.config(text="GAME OVER! Press SPACE to restart")
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            self.game_over_label.config(text="GAME OVER! Press SPACE to restart")
            return
        
        # Move snake
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
            self.update_score_display()
        else:
            self.snake.pop()
    
    def draw(self):
        """Draw the game"""
        self.canvas.delete("all")
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = self.SNAKE_HEAD_COLOR if i == 0 else self.SNAKE_COLOR
            self.canvas.create_rectangle(
                x * self.GRID_SIZE + 1,
                y * self.GRID_SIZE + 1,
                (x + 1) * self.GRID_SIZE - 1,
                (y + 1) * self.GRID_SIZE - 1,
                fill=color,
                outline=color
            )
        
        # Draw food
        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * self.GRID_SIZE + 1,
            fy * self.GRID_SIZE + 1,
            (fx + 1) * self.GRID_SIZE - 1,
            (fy + 1) * self.GRID_SIZE - 1,
            fill=self.FOOD_COLOR,
            outline=self.FOOD_COLOR
        )
    
    def update_score_display(self):
        """Update the score display"""
        self.score_label.config(text=f"Score: {self.score}")
    
    def game_loop(self):
        """Main game loop"""
        self.update()
        self.draw()
        
        if not self.game_over:
            self.root.after(100, self.game_loop)  # 100ms = ~10 FPS
        else:
            self.root.after(100, self.game_loop)  # Keep running to allow restart

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#1a1a1a")
    game = SnakeGame(root)
    root.mainloop()
