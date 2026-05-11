from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_num = random.uniform(20, 50)
            rotate_pos = self.velocity.rotate(rand_num)
            rotate_neg = self.velocity.rotate(rand_num * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_scaled_velocity = 1.2

            new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_1.velocity = rotate_pos * new_scaled_velocity
            new_asteroid_2.velocity = rotate_neg * new_scaled_velocity
