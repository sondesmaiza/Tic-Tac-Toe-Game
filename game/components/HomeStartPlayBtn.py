from constants.constants import blue, black, screen_width

def HomeStartPlayBtn(pygame, surface,change_screen):
    # Define the rectangle background (optional, for styling)

    rect = pygame.Rect(0, 450, screen_width, 350)  
    pygame.draw.rect(surface, blue, rect) 
    
    # Capsule button properties
    button_width = 300   # Adjust the width of the button
    button_height = 80   # Adjust the height of the button
    button_x = (screen_width - button_width) // 2  # Center the button horizontally
    button_y = 650  # Position vertically in the middle of the exit section
    button_y_2 = 500  # Position vertically in the middle of the exit section
    border_radius = button_height // 2  # Makes the rectangle fully rounded

    button_rect_border = pygame.Rect(button_x-2, button_y-2, button_width+4, button_height+4)
    pygame.draw.rect(surface, black, button_rect_border, border_radius=border_radius)
    # Draw the capsule-shaped button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(surface, blue, button_rect, border_radius=border_radius)



    # Button 2

    button_rect_border2 = pygame.Rect(button_x-2, button_y_2-2, button_width+4, button_height+4)
    pygame.draw.rect(surface, black, button_rect_border2, border_radius=border_radius)
    # Draw the capsule-shaped button
    button_rect2 = pygame.Rect(button_x, button_y_2, button_width, button_height)
    pygame.draw.rect(surface, blue, button_rect2, border_radius=border_radius)

    # Draw the capsule-shaped button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(surface, blue, button_rect, border_radius=border_radius)



    # Draw text inside the button
    font = pygame.font.Font(None, 40)  # Default font, size 40
    text = font.render("Play Vs AI", True, black)  # Render text in black
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))  # Center text in button
    surface.blit(text, text_rect)  # Draw text onto the surface

    # Draw text inside the button 2
    font = pygame.font.Font(None, 40)  # Default font, size 40
    text = font.render("Player Vs Player", True, black)  # Render text in black
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y_2 + button_height // 2))  # Center text in button
    surface.blit(text, text_rect)  # Draw text onto the surface

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
        change_screen("screen_main_game_vs_ai")

    if button_rect2.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
        change_screen("screen_main_game_player_vs_player")

    return button_rect  # Return button area for click detection


