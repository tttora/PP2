import pygame
from player import MusicPlayer


def main():
    pygame.init()
    pygame.mixer.init()

    player = MusicPlayer(800, 400, "music")

    clock = pygame.time.Clock()
    running = True

    while running:
        running = player.handle_events()
        player.update()
        player.draw()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()