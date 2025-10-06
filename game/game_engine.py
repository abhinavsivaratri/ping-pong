import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        # Task 2: Game State Variables
        self.max_score = 5
        self.game_state = "running"
        self.winner = None
     # Task 4: Load Sound Effects
        try:
            self.paddle_hit_sound = pygame.mixer.Sound("hit.wav")
            self.wall_bounce_sound = pygame.mixer.Sound("wall.wav")
            self.score_sound = pygame.mixer.Sound("score.wav")
        except pygame.error as e:
            print(f"Warning: Could not load sound files. Make sure hit.wav, wall.wav, and score.wav are in the project root. Error: {e}")
            self.paddle_hit_sound = None # Use None to prevent crashes if files are missing
            self.wall_bounce_sound = None
            self.score_sound = None

    def handle_input(self):
        # Only allow input if the game is running
        if self.game_state == "running":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(-10, self.height)
            if keys[pygame.K_s]:
                self.player.move(10, self.height)

    def check_win(self):
        if self.player_score >= self.max_score:
            self.game_state = "game_over"
            self.winner = "PLAYER"
        elif self.ai_score >= self.max_score:
            self.game_state = "game_over"
            self.winner = "AI"

    def update(self):
        if self.game_state == "running":
            self.ball.move()
            # Pass the engine instance for access to sound objects
            self.ball.check_collision(self.player, self.ai, self) 

            # Scoring logic - Play score sound here!
            if self.ball.x <= 0:
                self.ai_score += 1
                if self.score_sound: self.score_sound.play() # Play score sound
                self.ball.reset()
            elif self.ball.x >= self.width:
                self.player_score += 1
                if self.score_sound: self.score_sound.play() # Play score sound
                self.ball.reset()

            self.ai.auto_track(self.ball, self.height)
            self.check_win()

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width * 3//4, 20))
        
        # Task 2: Game Over Screen Display
        if self.game_state == "game_over":
            # ... (lines for rendering winner_text) ...

            prompt_font = pygame.font.SysFont("Arial", 25)
            prompt_line1 = prompt_font.render("CHOOSE NEW MAX SCORE (Press 3, 5, or 7)", True, WHITE)
            prompt_line2 = prompt_font.render("Press ESC to Exit", True, WHITE)

            rect1 = prompt_line1.get_rect(center=(self.width // 2, self.height // 2 + 60))
            rect2 = prompt_line2.get_rect(center=(self.width // 2, self.height // 2 + 100))

            screen.blit(prompt_line1, rect1)
            screen.blit(prompt_line2, rect2)
        # =================================================================
# File: game/game_engine.py
# New Method to add: reset_game
# =================================================================

    def reset_game(self, new_max_score):
        # Update the score target
        self.max_score = new_max_score
        
        # Reset scores and winner
        self.player_score = 0
        self.ai_score = 0
        self.winner = None
        
        # Reset ball and paddles
        self.ball.reset()
        self.player.reset(self.height) # Assumes reset method is added to Paddle
        self.ai.reset(self.height)     # Assumes reset method is added to Paddle

        # Set game state back to running
        self.game_state = "running"
        


