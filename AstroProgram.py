#!/usr/bin/env python 3
# AstroClock
# Ethan Dall & Steven Thompson
# 3-21-18

import os
import pygame
import math
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# time
walk = 0
type_x = 0
type_y = 0
move_sec = 0
move_min = 0
move_hr = 0
HYP = 180
timeCount = 0
timeSec = 1000
timeMin = 6000
timeHr = 3600000
rotate = 360
offset = 15
tm_sec = 0
tm_min = 0
tm_hr = 0

# dictionaries
numeral_dict = {}
zodiac_dict = {}

#Lists
zodiac_list = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]


def setxAngleAttribute(x_angle):
    x = (HYP * math.cos(math.radians(x_angle)))
    return x


def setyAngleAttribute(y_angle):
    y = (HYP * math.sin(math.radians(y_angle)))
    return y

# Starts Pygame

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)

# Fonts
name_font = pygame.font.SysFont('Times New Roman.ttf', 25)

pygame.display.set_caption("Astronomical Clock")

# Numbers to be drawn
for i in range(1, 25):
    val = i
    numeral = ''
    numeral += 'X' * (i // 10)
    if i % 10 == 9:
        numeral += 'IX'
        val -= 9
    else:
        cost = i % 10 // 5
        numeral += 'V' * cost
        val -= cost * 5

    if val % 5 == 4 and val != 9:
        numeral += 'IV'
    else:
        numeral += 'I' * (val % 5)

    numeral_dict[str(i)] = name_font.render(numeral, 1, (0, 0, 0))


class Clock(object):

    def __init__(self):
        self.hour24_face()
        self.hour_hands()
        self.zodiac_info()

    @staticmethod
    def hour24_face():
        # +200 because 200 is center and numbers to need to rotate around it
        for i in range(1, 25):
            coords = (270 + (offset * i)) % 360
            screen.blit(numeral_dict[str(i)], (setxAngleAttribute(coords) + 190, setyAngleAttribute(coords) + 190))

    @staticmethod
    def hour_hands():
        """Runs and Draws the Seconds-Hand"""
        secX = (HYP * math.cos(math.radians(move_sec))) + 200
        secY = (HYP * math.sin(math.radians(move_sec))) + 200
        pygame.draw.line(screen, RED, (200, 200), (secX, secY), 2)

        """Runs and Draws the Minutes-Hand"""
        minX = (HYP * math.cos(math.radians(move_min))) + 200
        minY = (HYP * math.sin(math.radians(move_min))) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (minX, minY), 3)

        """Runs and Draws the Hours-Hand"""
        hrX = (HYP * math.cos(math.radians(move_hr))/1.5) + 200
        hrY = (HYP * math.sin(math.radians(move_hr))/1.5) + 200
        pygame.draw.line(screen, BLACK, (200, 200), (hrX, hrY), 3)

    @staticmethod
    def zodiac_info():
        """Prints the appropriate info based on the sign"""
        # URL: http://www.astrology-zodiac-signs.com/

        # Aquarius
        zodiac_dict['Aquarius'] = 'Aquarius: \n' + 'Element: Air\n' + 'Compatible: Leo & Sagittarius\n' + 'Strengths: Progressive, Original, Independent, Humanitarian\n' + 'Weaknesses: Runs from emotional expression, Temperamental, Uncompromising, Aloof\n' + 'Likes: Fun with Friends, Helping Others, Fighting for causes, Intellectual Conversation, A good listener\n' + 'Dislikes: Limitations, Broken Promises, Being Lonely, Dull or Boring situation, Disagreements\n'

        # Pisces
        zodiac_dict['Pisces'] = 'Pisces: \n' + 'Element: Water\n' + 'Compatible: Virgo & Taurus\n' + 'Strengths: Compassionate, Artistic, Intuitive, Gentle, Wise, Musical\n' + 'Weaknesses: Fearful, Overly Trusting, Sadness, Desire to escape reality, Victimed or Martyred\n' + 'Likes: Being alone, Sleeping, Music, Romance, Visual Media, Swimming, Spiritual Themes\n' + 'Dislikes: Know-It-Alls, Criticism, Past Mistakes, Cruelty\n'

        # Aries
        zodiac_dict['Aries'] = 'Aries: \n' + 'Element: Fire\n' + 'Compatible: Libra & Leo\n' + 'Strengths: Courageous, Determined, Confident, Enthusiastic, Optimistic, Honest, Passionate\n' + 'Weaknesses: Impatient, Moody, Short-Tempered, Impulsive, Aggressive\n' + 'Likes: Comfortable clothes, Leadership, Physical challenge, Individual sports\n' + 'Dislikes: Inactivity, Delays, Work that does not use one\'s talents\n'

        # Taurus
        zodiac_dict['Taurus'] = 'Taurus: \n' + 'Element: Earth\n' + 'Compatible: Scorpio & Cancer\n' + 'Strengths: Reliable, patient, practical, devoted, responsible, stable\n' + 'Weaknesses: Stubborn, possessive, uncompromising\n' + 'Likes: Gardening, cooking, music, romance, high quality clothes, working with hands\n' + 'Dislikes: Sudden changes, complications, insecurity of any kind, synthetic fabrics\n'

        # Gemini
        zodiac_dict['Gemini'] = 'Gemini: \n' + 'Element: Air\n' + 'Compatible: Sagittarius & Aquarius\n' + 'Strengths: Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas\n' + 'Weaknesses: Nervous, inconsistent, indecisive\n' + 'Likes: Music, books, magazines, chats with nearly anyone, short trips around the town\n' + 'Dislikes: Being alone, being confined, repetition and routine\n'

        # Cancer
        zodiac_dict['Cancer'] = 'Cancer: \n' + 'Element: Water\n' + 'Compatible: Capricorn & Taurus\n' + 'Strengths: Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive\n' + 'Weaknesses: Moody, pessimistic, suspicious, manipulative, insecure\n' + 'Likes: Art, home-based hobbies, relaxing near or in water, helping loved ones, a good meal with friends\n' + 'Dislikes: Strangers, any criticism of Mom, revealing of personal life\n'

        # Leo
        zodiac_dict['Leo'] = 'Leo: \n' + 'Element: Fire\n' + 'Compatible: Aquarius & Gemini\n' + 'Strengths: Creative, passionate, generous, warm-hearted, cheerful, humorous\n' + 'Weaknesses: Arrogant, stubborn, self-centered, lazy, inflexible\n' + 'Likes: Theater, taking holidays, being admired, expensive things, bright colors, fun with friends\n' + 'Dislikes: Being ignored, facing difficult reality, not being treated like a king or queen\n'

        # Virgo
        zodiac_dict['Virgo'] = 'Virgo: \n' + 'Elements: Earth\n' + 'Compatible: Pisces & Cancer\n' + 'Strengths: Loyal, analytical, kind, hardworking, practical\n' + 'Weaknesses: Shyness, worry, overly critical of self and others, all work and no play\n' + 'Likes: Animals, healthy food, books, nature, cleanliness\n' + 'Dislikes: Rudeness, asking for help, taking center stage\n'

        # Libra
        zodiac_dict['Libra'] = 'Libra: \n' + 'Elements: Air\n' + 'Compatible: Aries & Sagittarius\n' + 'Strengths: Cooperative,diplomatic, gracious, fair-minded, social\n' + 'Weaknesses: Indecisive, avoids confrontations, will carry a grudge, self-pity\n' + 'Likes: Harmony, gentleness, sharing with others, the outdoors\n' + 'Dislikes: Violence, injustice, loudmouths, conformity\n'

        # Scorpio
        zodiac_dict['Scorpio'] = 'Scorpio: \n' + 'Elements: Water\n' + 'Compatible: Taurus & Cancer\n' + 'Strengths: Resourceful, brave, passionate, stubborn, a true friend\n' + 'Weaknesses: Distrusting, jealous, secretive, violent\n' + 'Likes: Truth, facts, being right, longtime friends, teasing, a grand passion\n' + 'Dislikes: Dishonesty, revealing secrets, passive people\n'

        # Sagittarius
        zodiac_dict['Sagittarius'] = 'Sagittarius: \n' + 'Elements: Fire\n' + 'Compatible: Gemini & Aries\n' + 'Strengths: Generous, idealistic, great sense of humor\n' + 'Weaknesses: Promises more than can deliver, very impatient, will say anything no matter how undiplomatic\n' + 'Likes: Freedom, travel, philosophy, being outdoors\n' + 'Dislikes: Clingy people, being constrained, off-the-wall theories, details\n'

        # Capricorn
        zodiac_dict['Capricorn'] = 'Capricorn: \n' + 'Elements: Earth\n' + 'Compatible: Taurus & Cancer\n' + 'Strengths: Responsible, disciplined, self-control, good managers\n' + 'Weaknesses: Know-it-all, unforgiving, condescending, expecting the worst\n' + 'Likes: Family, tradition, music, understated status, quality craftsmanship\n' + 'Dislikes: Almost everything at some point\n'

        # Prints all the Zodiac Descriptions
        '''for i in range(12):
            sign = zodiac_list[i]
            print(zodiac_dict[sign])'''

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

    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.circle(screen, BLACK, (200, 200), 200, 1)
    frame.hour_hands()
    frame.hour24_face()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Updates Seconds
    tm_sec = time.localtime()[5]
    move_sec = (tm_sec * 6 - 90) % 360

    # Updates Minutes
    tm_min = time.localtime()[4]
    if (tm_hr % 2) != 0:
        move_min = (tm_min * 3 + 90)
    else:
        move_min = (tm_min * 3 - 90) % 360

    # Updates Hours
    tm_hr = time.localtime()[3]
    if tm_min < 180:
        move_hr = (15 * tm_hr) - 90
    elif tm_min >= 180:
        move_hr = ((15 * tm_hr) - 90) * 2

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()