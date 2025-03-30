from constants.constants import blue, white, black

def draw_ExitGame(pygame, surface, screen_width):
    # Define the rectangle background (optional, for styling)
    rect = pygame.Rect(0, 590, screen_width, 210)  
    pygame.draw.rect(surface, white, rect)  # Background rectangle
    
    # Capsule button properties
    button_width = 200   # Adjust the width of the button
    button_height = 80   # Adjust the height of the button
    button_x = (screen_width - button_width) // 2  # Center the button horizontally
    button_y = 650  # Position vertically in the middle of the exit section
    border_radius = button_height // 2  # Makes the rectangle fully rounded

    # Draw the capsule-shaped button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(surface, blue, button_rect, border_radius=border_radius)

    # Draw text inside the button
    font = pygame.font.Font(None, 40)  # Default font, size 40
    text = font.render("Exit", True, black)  # Render text in black
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))  # Center text in button
    surface.blit(text, text_rect)  # Draw text onto the surface

    return button_rect  # Return button area for click detection
