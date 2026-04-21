import pygame
from constants import *
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    astrofield = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
   

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
