from constants.constants import *


def Background(pygame,screen):
    rect = pygame.Rect(0, 0, screen_width, 800)  
    pygame.draw.rect(screen, bg, rect) 