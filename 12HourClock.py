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

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Image Scaling and import
img = pygame.image.load(os.path.join("pictures", "analogClock.png"))
w, h = img.get_size()
img = pygame.transform.scale(img, (int(w * 1.785), int(h * 1.778)))

#Quadrants
Q1 = [190, 190]
Q2 = [-190, 190]
Q3 = [-190, -190]
Q4 = [190, -190]
QUAD = [Q1, Q2, Q3, Q4]

# time
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

    def facePlate(self):
        screen.blit(img, (0, 0))
        pygame.draw.ellipse(screen, BLACK, [0, 0, 400, 400], 3)

    def armTimes(self):
        # second hand
        for a in QUAD:
            i = 0
            j = 0
            while i <= a[0] and j <= a[1]:
                if a[0] > 0:
                    i += 12.667
                    if a[1] > 0:
                        j += 12.667
                    else:
                        j -= 12.667
                else:
                    i -= 12.667
                    if a[1] > 0:
                        j += 12.667
                    else:
                        j -= 12.667
                yield i, j


        #  comment before it


frame = Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
arms = frame.armTimes()

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
    try:
        new_pos = next(arms)
    except StopIteration:
        arms = frame.armTimes()
        new_pos = next(arms)

    pygame.draw.line(screen, RED, (200, 200), new_pos, 2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
