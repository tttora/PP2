import pygame
from ball import Ball


def main():
    pygame.init()

    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Moving Red Ball")

    clock = pygame.time.Clock()
    ball = Ball(400, 300, 25, 20, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -ball.step)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, ball.step)
                elif event.key == pygame.K_LEFT:
                    ball.move(-ball.step, 0)
                elif event.key == pygame.K_RIGHT:
                    ball.move(ball.step, 0)

        screen.fill((255, 255, 255))
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()