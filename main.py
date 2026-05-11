import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()
    player = Player(player_x, player_y)


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player.position):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot.position):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

        

if __name__ == "__main__":
    main()
