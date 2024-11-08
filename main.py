import pygame
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_SCORE 

def main():
    print("Starting asteroids!")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")
    pygame.init()
    score = 0
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
# start game loop
    while True:
        if score >= TARGET_SCORE:
            print("You win!🏅")
            return 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        score_text = font.render(f"Score: {score}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        
        for member in updatable:
            member.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    score = asteroid.split(score)

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
