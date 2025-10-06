import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall bounce collision (vertical)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            # Task 4: Play wall bounce sound
            # NOTE: We can't play sound here directly because the Ball class doesn't know about GameEngine.
            # This is a design flaw that the prompt encourages you to fix, but for simplicity, we'll
            # stick to passing the engine instance through check_collision and handle sound there.
            self.velocity_y *= -1

# =================================================================
# File: game/ball.py
# Method: check_collision
# =================================================================

    def check_collision(self, player, ai, engine): # ADD 'engine' argument
        ball_rect = self.rect()
        hit = False

        # Check collision with Player Paddle (left side)
        if ball_rect.colliderect(player.rect()):
            if self.velocity_x < 0:
                self.velocity_x *= -1
                self.x = player.x + player.width
                hit = True

        # Check collision with AI Paddle (right side)
        elif ball_rect.colliderect(ai.rect()):
            if self.velocity_x > 0:
                self.velocity_x *= -1
                self.x = ai.x - self.width
                hit = True
        
        # Check collision with top/bottom walls (re-check the logic from move to play sound)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            if engine.wall_bounce_sound:
                engine.wall_bounce_sound.play()

        # Play paddle hit sound if a paddle was hit
        if hit and engine.paddle_hit_sound:
            engine.paddle_hit_sound.play()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
