import pygame
import ctypes
import game
import math

# Get screen size
user32 = ctypes.windll.user32
screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# TODO Define window size
WIDTH = 1080
HEIGHT = 720

# Initialisation pygame
pygame.init()

# Display initialisation
pygame.display.set_caption("BomberMan")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# TODO Import Background

# TODO Import Start button

#Keep the window opened
running = True
while running:
  for event in pygame.event.get():
        # END condition
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
