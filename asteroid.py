from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 
        
        angle = random.uniform(20, 50)
        vel_1 = self.velocity.rotate(angle)
        vel_2 = self.velocity.rotate(-angle)
        rad = self.radius - ASTEROID_MIN_RADIUS
        a_1 = Asteroid(self.position.x, self.position.y, rad)
        a_2 = Asteroid(self.position.x, self.position.y, rad)
        a_1.velocity = vel_1 * 1.2
        a_2.velocity = vel_2 * 1.2
