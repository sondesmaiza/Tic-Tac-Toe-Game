from constants.constants import *

def TextPresent(pygame,screen):
    rect = pygame.Rect(0, 0, screen_width, 800)  
    pygame.draw.rect(screen, bg, rect)

    font = pygame.font.Font(None, font_size)
    text1 = font.render('The winner of this', True, black)
    text_rect1 = text1.get_rect(center=(screen_width // 2, 75))  # Center the text
    screen.blit(text1, text_rect1)

    text2 = font.render('Round is', True, black)
    text_rect2 = text1.get_rect(center=(270, 110))  # Center the text
    screen.blit(text2, text_rect2)

def WinnerShow(pygame,screen,winner):
    button_width = 300   # Adjust the width of the button
    button_height = 80   # Adjust the height of the button
    button_x = (screen_width - button_width) // 2  # Center the button horizontally
    button_y = 170  # Position vertically in the middle of the exit section
    border_radius = 30  # Makes the rectangle fully rounded

    button_rect_border = pygame.Rect(button_x-2, button_y-2, button_width+4, button_height+4)
    pygame.draw.rect(screen, black, button_rect_border, border_radius=border_radius)

    # Draw the capsule-shaped button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, blue, button_rect, border_radius=border_radius)

    font = pygame.font.Font(None, 40)  # Default font, size 40
    text = font.render(winner, True, black)  # Render text in black
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))  # Center text in button
    screen.blit(text, text_rect)  # Draw text onto the surface


def ReplayGame(pygame, surface,reset_game):
    # Define the rectangle background (optional, for styling)

    rect = pygame.Rect(0, 570, screen_width, 230)  
    pygame.draw.rect(surface, blue, rect) 
    
    # Capsule button properties
    button_width = 300   # Adjust the width of the button
    button_height = 80   # Adjust the height of the button
    button_x = (screen_width - button_width) // 2  # Center the button horizontally
    button_y = 650  # Position vertically in the middle of the exit section
    border_radius = button_height // 2  # Makes the rectangle fully rounded

    button_rect_border = pygame.Rect(button_x-2, button_y-2, button_width+4, button_height+4)
    pygame.draw.rect(surface, black, button_rect_border, border_radius=border_radius)

    # Draw the capsule-shaped button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(surface, blue, button_rect, border_radius=border_radius)



    # Draw text inside the button
    font = pygame.font.Font(None, 40)  # Default font, size 40
    text = font.render("Play Again :D", True, black)  # Render text in black
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))  # Center text in button
    surface.blit(text, text_rect)  # Draw text onto the surface

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
        reset_game()

    return button_rect  # Return button area for click detection


def Screen_Winner(pygame,screen,winner,reset_game):
    TextPresent(pygame,screen)
    WinnerShow(pygame,screen,winner)
    ReplayGame(pygame,screen,reset_game)



    
    