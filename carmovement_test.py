#Eine Chat GTP Lösung

import pygame
import random

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a rectangle object
rect = pygame.Rect(0, 0, 50, 50)

# Target point
target_x = random.randint(0, 750)
target_y = random.randint(0, 550)

# Speed in pixels per frame
speed = 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move rectangle towards target point
    if rect.x < target_x:
        rect.x += speed
    elif rect.x > target_x:
        rect.x -= speed

    if rect.y < target_y:
        rect.y += speed
    elif rect.y > target_y:
        rect.y -= speed

    # Check if rectangle has reached target point
    if rect.x == target_x and rect.y == target_y:
        target_x = random.randint(0, 750)
        target_y = random.randint(0, 550)

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the rectangle
    pygame.draw.rect(screen, (0, 0, 0), rect)

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()

