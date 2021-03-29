import pygame
import ctypes
import game
import math
from pygame_widgets import Button




# Get screen size
user32 = ctypes.windll.user32
screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Init clock
clock = pygame.time.Clock()
FPS = 60

# TODO Define window size
WIDTH = 1080
HEIGHT = 720

#Init a game
game = game.Game(1,(WIDTH,HEIGHT))

# Initialisation pygame
pygame.init()

# Display initialisation
pygame.display.set_caption("BomberMan")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def clicked(button) :
    button.hide()
    game.start()

#Create the start Button 
start_button = Button(
            screen, WIDTH/2-50, HEIGHT/2-50, 100, 100, text='Start',
            fontSize=50, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick = lambda : game.start()     #run game.start() when the button is clicked
            onClick = lambda : clicked(start_button)     #run game.start() when the button is clicked
         )


# TODO Import Background

# TODO Import Start button

# Keep the window opened
running = True
while running:
    screen.fill((15,15,15)) #fill the screen in black
    events = pygame.event.get()
    for event in events:
        # END condition
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
    #run only if the loop didn't break
    else: 
        if(game._is_playing):
            #When the game is not over
            game.update(screen)        
        else :
            #When in the "Menu"
            start_button.listen(events)
            start_button.draw()
        pygame.display.update()
    clock.tick(FPS)
