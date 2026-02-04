import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Colored Window")

bg_color = (0, 150, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bg_color)
    pygame.display.update()

pygame.quit()
sys.exit()