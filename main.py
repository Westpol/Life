import pygame


screen = None
width = None
height = None


def window_init():
    global screen, width, height
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Life")
    width, height = pygame.display.get_window_size()


def main_loop():
    while 1:
        pass


if __name__ == "__main__":
    window_init()
    main_loop()
