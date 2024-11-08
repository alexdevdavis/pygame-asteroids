import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCORE_INCREMENT, TARGET_SCORE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, score):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            score += SCORE_INCREMENT
            return score
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(angle * -1)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius )
        asteroid2 = Asteroid(self.position.x, self.position.y, radius )
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2
        return score
