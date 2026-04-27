import pygame
import sys
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

current_color = BLACK
current_tool = "brush"

drawing = False
start_pos = None
brush_size = 8

font = pygame.font.SysFont("Verdana", 18)


def draw_text():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 40))

    text = font.render(
        f"Tool: {current_tool} | B Brush | R Rect | C Circle | E Eraser | 1-5 Colors",
        True,
        BLACK
    )

    screen.blit(text, (10, 10))

def draw_rectangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    pygame.draw.rect(surface, color, (left, top, width, height), 3)


def draw_circle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

    pygame.draw.circle(surface, color, start, radius, 3)


running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                current_tool = "brush"

            elif event.key == pygame.K_r:
                current_tool = "rectangle"

            elif event.key == pygame.K_c:
                current_tool = "circle"

            elif event.key == pygame.K_e:
                current_tool = "eraser"

            elif event.key == pygame.K_1:
                current_color = BLACK

            elif event.key == pygame.K_2:
                current_color = RED

            elif event.key == pygame.K_3:
                current_color = GREEN

            elif event.key == pygame.K_4:
                current_color = BLUE

            elif event.key == pygame.K_5:
                current_color = WHITE

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                if current_tool == "rectangle":
                    draw_rectangle(screen, current_color, start_pos, end_pos)

                elif current_tool == "circle":
                    draw_circle(screen, current_color, start_pos, end_pos)

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "brush":
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)

                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size * 2)

    draw_text()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()