import pygame
import sys
# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Image")

# Load image
image = pygame.image.load("image.png")
image_rect = image.get_rect()
image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Movement speed
speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    # Fill background
    screen.fill((255, 255, 255))

    # Draw image
    screen.blit(image, image_rect)

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()