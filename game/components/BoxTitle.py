from constants.constants import black,blue,font_size,screen_height,screen_width


def draw_rounded_rect(pygame, surface, color, rect, radius):
    # Draw the main rectangle with no rounded corners (background)
    pygame.draw.rect(surface, color, rect, border_radius=radius)  # Use border_radius for rounded corners

    # Optional: Drawing a rounded rectangle manually if you need to control it more
    # You can skip this if the above pygame.draw.rect() works well for you
    pygame.draw.arc(surface, color, pygame.Rect(rect.left, rect.bottom - radius * 2, radius * 2, radius * 2), 1.57, 3.14, radius)  # Bottom-left corner
    pygame.draw.arc(surface, color, pygame.Rect(rect.right - radius * 2, rect.bottom - radius * 2, radius * 2, radius * 2), 0, 1.57, radius)  # Bottom-right corner
    pygame.draw.rect(surface, color, pygame.Rect(rect.left + radius, rect.bottom - radius, rect.width - radius * 2, radius))

def BoxTitle(pygame, screen):
    rect = pygame.Rect(0, 0, screen_width, 150)  # Rectangle with width and height
    draw_rounded_rect(pygame, screen, blue, rect, 20)  # Draw rounded rectangle with radius 20

    font = pygame.font.Font(None, font_size)
    text = font.render('Tic-Tac-Toe Game', True, black)
    text_rect = text.get_rect(center=(screen_width // 2, 75))  # Center the text
    screen.blit(text, text_rect)