import pygame
from game.game_engine import GameEngine

# Task 4: Initialize the mixer for sound BEFORE pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512) # Optional: improves sound latency
pygame.init()

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN: # Check for any key press
                if engine.game_state == "game_over":
                    # Task 3: Handle Replay Input
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_3:
                        engine.reset_game(3)
                    elif event.key == pygame.K_5:
                        engine.reset_game(5)
                    elif event.key == pygame.K_7:
                        engine.reset_game(7)

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()