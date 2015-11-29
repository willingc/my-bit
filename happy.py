"""
happy.py

by Carol Willing
November 28, 2015
Public Domain

Use this to display an image on micro:bit's 5x5 pixel grid of LEDs.

We'll use the brightness setting of an LED to add creativity to image.

    Brightness:
        9 for a bold outline (brightest)
        6 for adding details (medium)
        2 for shading        (dim light)
        0 for off            (no light)

Remember...
Writing a program is similar to planning a birthday party.
    Program     Birthday party
    -------     --------------
    'Prepare'   Prepare the room with balloons; order food; pick up a cake.
    'Do'        Do things during the party -- sing, dance, play videogames.
    'Clean'     Clean the table. Tidy up after the party. Take out the rubbish.

"""
from microbit import *

# Prepare stuff
my_happy_face = Image.HAPPY

# Do stuff
display.show(my_happy_face)
sleep(8000)

# Clean up stuff (yeah, you should clean your room too)
display.clear()
display.scroll("BYE")
sleep(1000)
display.clear()
