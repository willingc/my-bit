"""
happy.py

by Carol Willing
November 28, 2015
Public Domain

Use this to display a 'Happy Face' image on micro:bit's 5x5 pixel grid of LEDs.

Remember... Writing a program is similar to planning a birthday party.

Program       Birthday party
-------       --------------
'Prepare'     Prepare the room with balloons; order food; pick up a cake.
'Do'          Do things during the party -- sing, dance, play videogames.
'Clean'       Clean the table. Tidy up after the party. Take out the rubbish.

"""
from microbit import *

# Prepare. Put the preinstalled images into user friendly variables
my_happy_face = Image.HAPPY
my_sad_face = Image.SAD

# Do things! ----> Show the images on the display.
display.show(my_happy_face)
sleep(8000)

display.show(my_sad_face)
sleep(8000)

display.show(my_happy_face)
sleep(4000)

# Clean up stuff. Display 'BYE' and clear display. (Clean your room too.)
display.scroll("BYE")
display.clear()
