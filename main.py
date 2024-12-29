"""Main file for the asteroids game."""
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from shot import Shot

def main():
    """Main function for the game."""
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    # Create game objects
    _player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _asteroid_field = AsteroidField()
    # Main game loop
    while True:
        # Clear the screen
        screen.fill((0, 0, 0))
        # Update and draw all sprites
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        # Check for collisions
        for asteroid in asteroids:
            if _player.collides_with(asteroid):
                print("Game over!!")
                pygame.quit()
                return
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.kill()
                    shot.kill()
        # Update the display
        pygame.display.flip()
        # Handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
