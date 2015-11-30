"""
faces.py

by Carol Willing
November 29, 2015
Public Domain

Use this to display happy or sad faces on micro:bit's 5x5 pixel grid of LEDs
when a user presses the micro:bit's A or B buttons.

Remember the major sections of a program: Prepare. Do. Clean up.

Prepare:  Put face images into variables. Create some variables for counting.
Do:       Give instructions. Loop and display faces. Share game statistics.
Clean up: Say bye and clear display.

"""
# Import the micro:bit library
from microbit import *

# --------
# Prepare!
# --------
my_happy_face = Image.HAPPY
my_sad_face = Image.SAD

# Let's track time and count the displayed faces starting at zero.
time_played = 0
count_happy_faces = 0
count_sad_faces = 0

# ----------
# Do things!
# ----------
# Give instructions.
display.scroll("Hi!")
sleep(8000)
display.scroll("If happy, press A button.")
sleep(8000)
display.scroll("If sad, press B button.")
sleep(8000)
display.scroll("To quit and exit, press both A and B at the same time.")
sleep(8000)


# Use a loop.
#    'wait' for button presses.
#    'check' if button is pressed.
#    'act' by showing a face.
#    Repeat until both buttons are pressed at the same time.
while not (button_a.is_pressed() and button_b.is_pressed()):
    if button_a.is_pressed():
        display.show(my_happy_face)
        count_happy_faces += 1
        sleep(8000)
        display.clear()

    if button_b.is_pressed():
        display.show(my_sad_face)
        count_sad_faces += 1
        sleep(8000)
        display.clear()

# Share game statistics.
#     Use micro:bit's built-in function, running_time(),
#     to estimate time_played.
time_played = running_time()
display.scroll("Time spent playing: ")
display.scroll(time_played)
display.scroll("smiles = ")
display.scroll(count_happy_faces)
display.scroll("frowns = ")
display.scroll(count_sad_faces)
sleep(8000)

# ---------
# Clean up!
# ---------
display.scroll("Bye.")
display.clear()
