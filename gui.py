import pygame
import sys
pygame.init()

SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe')
TITLE_FONT = pygame.font.SysFont('cambria', 200)
BG_COLOR = (180, 180, 180)
LINE_COLOR = (0, 0, 0)



while True:
    SCREEN.fill(BG_COLOR)
    # Horizontal lines
    pygame.draw.line(SCREEN, LINE_COLOR, (100, 300), (700, 300), 5)
    pygame.draw.line(SCREEN, LINE_COLOR, (100, 500), (700, 500), 5)
    # Vertical lines
    pygame.draw.line(SCREEN, LINE_COLOR, (300, 100), (300, 700), 5)
    pygame.draw.line(SCREEN, LINE_COLOR, (500, 100), (500, 700), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()