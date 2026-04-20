import pygame


class Ball:
    def __init__(self, x, y, radius, step, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.step = step
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (255, 0, 0)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)