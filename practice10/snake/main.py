import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
TOP_PANEL = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Colors
BG = (22, 24, 29)
PANEL = (35, 38, 46)
GRID = (45, 48, 56)
SNAKE_HEAD = (90, 220, 120)
SNAKE_BODY = (50, 170, 90)
FOOD_COLOR = (240, 80, 80)
WHITE = (245, 245, 245)
YELLOW = (255, 210, 80)
RED = (220, 60, 60)

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 48)

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
next_direction = "RIGHT"

food = None

score = 0
level = 1
speed = 8
foods_for_next_level = 3


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID, (x, TOP_PANEL), (x, HEIGHT))

    for y in range(TOP_PANEL, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y))


def draw_snake():
    for index, part in enumerate(snake):
        x, y = part

        if index == 0:
            color = SNAKE_HEAD
        else:
            color = SNAKE_BODY

        pygame.draw.rect(
            screen,
            color,
            (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4),
            border_radius=6
        )


def draw_food():
    x, y = food

    pygame.draw.circle(
        screen,
        FOOD_COLOR,
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        CELL_SIZE // 2 - 3
    )

    pygame.draw.circle(
        screen,
        YELLOW,
        (x + CELL_SIZE // 2 - 3, y + CELL_SIZE // 2 - 3),
        4
    )


def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(TOP_PANEL, HEIGHT, CELL_SIZE)

        new_food = (x, y)

        if new_food not in snake:
            return new_food


def draw_panel():
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, TOP_PANEL))

    title = font.render("Snake Game", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    speed_text = font.render(f"Speed: {speed}", True, WHITE)

    screen.blit(title, (20, 18))
    screen.blit(score_text, (240, 18))
    screen.blit(level_text, (370, 18))
    screen.blit(speed_text, (480, 18))


def game_over():
    screen.fill(BG)

    text1 = big_font.render("GAME OVER", True, RED)
    final_score = font.render(f"Final Score: {score}", True, WHITE)
    final_level = font.render(f"Level Reached: {level}", True, WHITE)

    screen.blit(text1, (150, 220))
    screen.blit(final_score, (220, 300))
    screen.blit(final_level, (220, 335))

    pygame.display.update()
    pygame.time.delay(2500)

    pygame.quit()
    sys.exit()


food = generate_food()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"

    direction = next_direction

    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # Wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < TOP_PANEL or head_y >= HEIGHT:
        game_over()

    # Snake body collision
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    if new_head == food:
        score += 1

        if score % foods_for_next_level == 0:
            level += 1
            speed += 2

        food = generate_food()

    else:
        snake.pop()

    screen.fill(BG)

    draw_grid()
    draw_snake()
    draw_food()
    draw_panel()

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()