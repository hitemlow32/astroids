import pygame
from constants import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    FPS = 60

    while 0 != 1 :
        ## allows the GUI to end the buttom if the x is clicked ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip() 
        dt = clock.tick(FPS) / 1000

    pygame.quit()
main()