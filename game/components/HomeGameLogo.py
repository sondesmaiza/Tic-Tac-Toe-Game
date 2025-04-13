from constants.constants import *


def HomeGameLogo(pygame,screen):
    rect = pygame.Rect(50, 50, 300, 300)  
    pygame.draw.rect(screen, bg, rect) 

    logo_image = pygame.image.load("images/tictactoe.png")  

    logo_image = pygame.transform.scale(logo_image, (rect.width, rect.height))

    screen.blit(logo_image, (rect.x, rect.y))

    font = pygame.font.Font(None, font_size)
    font.set_underline(True)
    text = font.render('Tic-Tac-Toe Game', True, black)
    text_rect = text.get_rect(center=(screen_width // 2, 400))  # Center the text
    screen.blit(text, text_rect)