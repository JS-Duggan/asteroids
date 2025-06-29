from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame

def main():
    # Game start message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}") 
    
    # Init pygame and clock
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # Set Screeen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create containers for game objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    # Add containers to game object classes 
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable)

    # Init game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        # Update and Draw game objects
        updateable.update(dt)
        for object in drawable:
            object.draw(screen)

        # Set FPS 
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

