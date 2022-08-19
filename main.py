import pygame
import sys
pygame.init()

SCREEN = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe')
TITLE_FONT = pygame.font.SysFont('cambria', 200)
BG_COLOR = (50, 100, 200)

while True:
    SCREEN.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()