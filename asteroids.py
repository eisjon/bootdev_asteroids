#
import pygame
from logger import log_event
import random
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroids(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20,50)
        #print("velocity:", self.velocity)
        new_vel_1 = self.velocity.rotate(rand)
        #print("new_vel_1:", new_vel_1)
        new_vel_2 = self.velocity.rotate(rand * -1)
        #print("new_vel_2:", new_vel_2)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroids(self.position[0], self.position[1], new_radius)
        asteroid.velocity = new_vel_1 * 1.2
        asteroid = Asteroids(self.position[0], self.position[1], new_radius)
        asteroid.velocity = new_vel_2 * 1.2
        
