from re import S
import pygame
import sys
pygame.init()

SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe')
TITLE_FONT = pygame.font.SysFont('cambria', 120)
PROMPT_FONT = pygame.font.SysFont('cambria', 40)
BG_COLOR = (180, 180, 180)
LINE_COLOR = (0, 0, 0)
# Title
TITLE = TITLE_FONT.render("TIC TAC TOE", True, (0, 0, 0))
TITLE_RECT = TITLE.get_rect(center=(400, 100))
# Prompt 1
PROMPT_I = PROMPT_FONT.render("Press 'SPACE' to play.", True, (0, 0, 0))
P_I_RECT = PROMPT_I.get_rect(center=(400, 400))
# Prompt 2
PROMPT_II = PROMPT_FONT.render("Press 'ESCAPE' to exit.", True, (0, 0, 0))
P_II_RECT = PROMPT_II.get_rect(center=(400, 500))


def menu():
    while True:
        SCREEN.fill(BG_COLOR)
        SCREEN.blit(TITLE, TITLE_RECT)
        SCREEN.blit(PROMPT_I, P_I_RECT)
        SCREEN.blit(PROMPT_II, P_II_RECT)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def play():
    while True:
        SCREEN.fill(BG_COLOR)
        # Horizontal lines
        pygame.draw.line(SCREEN, LINE_COLOR, (100, 300), (700, 300), 5)
        pygame.draw.line(SCREEN, LINE_COLOR, (100, 500), (700, 500), 5)
        # Vertical lines
        pygame.draw.line(SCREEN, LINE_COLOR, (300, 100), (300, 700), 5)
        pygame.draw.line(SCREEN, LINE_COLOR, (500, 100), (500, 700), 5)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

menu()