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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)
SIENNA = (160,82,45)


x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1


def draw_stick_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, RED, [40 + x, 200 + ball_pos + y, 40, 40])

    pygame.draw.line(screen, BLACK, [200 + x, 350 + y], [200 + x, 500 + y], 5)

    pygame.draw.line(screen, BLACK, [200 + x, 400 + y], [120 + x, 400 + y], 5)

    pygame.draw.line(screen, BLACK, [200 + x, 400 + y], [120 + x, 400 + y], 5)

    pygame.draw.line(screen, BLACK, [200 + x, 500 + y], [100 + x, 650 + y], 5)

    pygame.draw.line(screen, BLACK, [200 + x, 500 + y], [250 + x, 650 + y], 5)

    pygame.draw.circle(screen, BLACK, [200 + x, 225 + y], 100)

    pygame.draw.circle(screen, SIENNA, [200 + x, 250 + y], 100)

    pygame.draw.circle(screen, BLACK, [135 + x, 235 + y], 15)

    pygame.draw.circle(screen, BLACK, [240 + x, 230 + y], 15)

    pygame.draw.ellipse(screen, BLACK, [175 + x, 300 + y, 40, 15])

# Loop as long as done == False
while not done:
    ball_pos += ball_change
    if ball_pos > 300:
        ball_change -= 30
    elif ball_pos < 25:
        ball_change += 30


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -10
    if keys[pygame.K_RIGHT]:
        x_speed = 10
    if keys[pygame.K_UP]:
        y_speed = -10
    if keys[pygame.K_DOWN]:
        y_speed = 10

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0


    PI = 3.141592653

    screen.fill(WHITE)

    draw_stick_stick_figure(screen, x_coord, y_coord)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()









