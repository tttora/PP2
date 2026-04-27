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

BG = (22, 24, 29)
PANEL = (35, 38, 46)
GRID = (45, 48, 56)
SNAKE_HEAD = (90, 220, 120)
SNAKE_BODY = (50, 170, 90)
RED = (230, 70, 70)
YELLOW = (240, 200, 70)
PURPLE = (180, 80, 220)
WHITE = (245, 245, 245)

font = pygame.font.SysFont("Verdana", 18)
big_font = pygame.font.SysFont("Verdana", 48)

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
next_direction = "RIGHT"

score = 0
level = 1
speed = 8
foods_for_next_level = 4

food = None


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


def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(TOP_PANEL, HEIGHT, CELL_SIZE)

        position = (x, y)

        if position not in snake:
            weight = random.choice([1, 2, 3])

            if weight == 1:
                color = RED
                lifetime = 5000
            elif weight == 2:
                color = YELLOW
                lifetime = 4000
            else:
                color = PURPLE
                lifetime = 3000

            return {
                "pos": position,
                "weight": weight,
                "color": color,
                "created_time": pygame.time.get_ticks(),
                "lifetime": lifetime
            }


def draw_food():
    x, y = food["pos"]
    weight = food["weight"]

    radius = 5 + weight * 3

    pygame.draw.circle(
        screen,
        food["color"],
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        radius
    )

    value_text = font.render(str(weight), True, WHITE)
    screen.blit(value_text, (x + 5, y - 1))


def check_food_timer():
    global food

    current_time = pygame.time.get_ticks()

    if current_time - food["created_time"] > food["lifetime"]:
        food = generate_food()


def draw_panel():
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, TOP_PANEL))

    current_time = pygame.time.get_ticks()
    time_left = max(0, food["lifetime"] - (current_time - food["created_time"]))
    seconds_left = time_left // 1000 + 1

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    speed_text = font.render(f"Speed: {speed}", True, WHITE)
    timer_text = font.render(f"Food: {seconds_left}s", True, WHITE)

    screen.blit(score_text, (15, 18))
    screen.blit(level_text, (150, 18))
    screen.blit(speed_text, (280, 18))
    screen.blit(timer_text, (420, 18))


def game_over():
    screen.fill(BG)

    text = big_font.render("GAME OVER", True, RED)
    final_score = font.render(f"Final Score: {score}", True, WHITE)
    final_level = font.render(f"Level Reached: {level}", True, WHITE)

    screen.blit(text, (145, 220))
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

    check_food_timer()

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

    if head_x < 0 or head_x >= WIDTH or head_y < TOP_PANEL or head_y >= HEIGHT:
        game_over()

    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    if new_head == food["pos"]:
        score += food["weight"]

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