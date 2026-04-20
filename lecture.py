import sys
import pygame
pygame.init()

sc = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

clock = pygame.time.Clock()

WHITE = (255,255,255)
PINK = (155,182,193)
pygame.draw.rect(sc, WHITE, (20, 20, 100, 100))
pygame.draw.line(sc, PINK, (200,20), (350, 50), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(60)
