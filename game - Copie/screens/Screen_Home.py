from constants.constants import *
from components.Background import Background
from components.HomeGameLogo import HomeGameLogo
from components.HomeStartPlayBtn import HomeStartPlayBtn



def Screen_Home(pygame,screen,change_screen):
    Background(pygame,screen)
    HomeGameLogo(pygame,screen)
    HomeStartPlayBtn(pygame,screen,change_screen)