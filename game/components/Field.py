from constants.constants import blue,font_size,black,bg

mini_box_width = 100
mini_box_height = 100

def draw_Field(pygame, screen, screen_width, game,PlaceMove,change_screen,to_winner_screen):
    # Define the rectangle for the red box with 100% width and 500 height
    red_box = pygame.Rect(0, 150, screen_width, 500)
    
    # Fill the red rectangle
    pygame.draw.rect(screen, bg, red_box) 



    

    for i in range(len(game)):
        for j in range(len(game[i])):
            draw_one_box(i,j,pygame, screen,game,PlaceMove,change_screen,to_winner_screen)
        


def draw_one_box(i,j,pygame, screen,game,PlaceMove,change_screen,to_winner_screen):

    x = 25 + i * (mini_box_width + 25)
    y = 150 + 20 + 25 + j * (mini_box_height + 25)
    value = game[i][j]

    box = pygame.Rect(x, y, mini_box_width, mini_box_width)
    pygame.draw.rect(screen, blue, box)

    center_box_x = x + (mini_box_width // 2) 
    center_box_y = y + (mini_box_height // 2) 

    font = pygame.font.Font(None, font_size)
    text = font.render(value, True, black)
    text_rect = text.get_rect(center=(center_box_x,center_box_y))  # Center the text
    screen.blit(text, text_rect)

    
    # Check for mouse click on the box
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if box.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
        print("Clicked on box",i,j)
        PlaceMove(i,j,change_screen,to_winner_screen,game)

   