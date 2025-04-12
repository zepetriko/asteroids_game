import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)


        
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()