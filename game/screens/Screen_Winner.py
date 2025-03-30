from constants.constants import *


def Screen_Winner(pygame,screen):
    rect = pygame.Rect(0, 0, screen_width, 800)  
    pygame.draw.rect(screen, (0,255,0), rect) 
    