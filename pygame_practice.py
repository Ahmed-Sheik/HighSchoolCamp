"""
title: pygame_practice
author: Ahmed
date: 2019-06-14 09:48
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (800, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BROWN = (165, 42, 42)
    SIENNA = (160,82,45)


    PI = 3.141592653

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [200, 350], [200, 500], 5)

    pygame.draw.line(screen, BLACK, [200, 400], [160, 400], 5)

    pygame.draw.line(screen, BLACK, [200, 400], [240, 400], 5)

    pygame.draw.line(screen, BLACK, [200, 500], [100, 650], 5)

    pygame.draw.line(screen, BLACK, [200, 500], [250, 650], 5)

    pygame.draw.circle(screen, BLACK, [200, 225], 100)

    pygame.draw.circle(screen, SIENNA, [200, 250], 100)

    pygame.draw.circle(screen, BLACK, [135, 235], 15)

    pygame.draw.circle(screen, BLACK, [240, 230], 15)

    pygame.draw.ellipse(screen, BLACK, [175, 300, 40, 15])










    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()









