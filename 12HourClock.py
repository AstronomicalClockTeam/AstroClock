"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import os
import pygame
import math
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Image Scaling and import
img = pygame.image.load(os.path.join("pictures", "analogClock.png"))
w, h = img.get_size()
img = pygame.transform.scale(img, (int(w * 1.785), int(h * 1.778)))

# time
move_sec = 0
move_min = 0
move_hr = 0
HYP = 190
timeCount = 0
timeSec = 1000
timeMin = 6000
timeHr = 3600000

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("12 Hour Clock")


class Clock(object):

    def __init__(self):
        self.facePlate()
        self.armTimes()

    def facePlate(self):
        screen.blit(img, (0, 0))
        pygame.draw.ellipse(screen, BLACK, [0, 0, 400, 400], 3)

    def armTimes(self):
        # Runs and Draws the Seconds-Hand
        secX = (HYP * math.cos(math.radians(move_sec))) + 200
        secY = (HYP * math.sin(math.radians(move_sec))) + 200
        pygame.draw.line(screen, RED, (200, 200), (secX, secY), 2)

        # Runs and Draws the Minutes-Hand
        minX = (HYP * math.cos(math.radians(move_min))) + 200
        minY = (HYP * math.sin(math.radians(move_min))) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (minX, minY), 3)

        # Runs and Draws the Hours-Hand
        hrX = (HYP * math.cos(math.radians(move_hr))/1.5) + 200
        hrY = (HYP * math.sin(math.radians(move_hr))/1.5) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (hrX, hrY), 3)


frame = Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    frame.facePlate()
    frame.armTimes()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Updates Seconds
    tm_sec = time.localtime()[5]
    move_sec = (tm_sec * 6 - 90) % 360

    # Updates Minutes
    tm_min = time.localtime()[4]
    move_min = (tm_min * 6 - 90) % 360

    # Updates Hours
    tm_hr = time.localtime()[3]
    move_hr = (((tm_min // 12) * 6) + ((tm_hr % 12) * 30) - 90) % 360


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
