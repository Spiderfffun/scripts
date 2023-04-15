import pygame                      # WARNING DO NOT LOOK THRU THIS CODE IT HAS MIXING OF "" AND ''
from PIL import Image
import sys
import threading
from guizero import App, Text, TextBox, Combo, PushButton
from tkinter import messagebox
import os

with Image.open('screenshot.png') as im:
    width, height = im.size

width_of_screenshot = width
height_of_screenshot = height
div = 1 if len(sys.argv) == 1 else int(sys.argv[1])

pygame.init()

commands = []

# Set up the Pygame window
screen = pygame.display.set_mode((width_of_screenshot // div, height_of_screenshot // div))

# Load screenshot.png
screenshot = pygame.image.load('screenshot.png')

# Resize screenshot to fit Pygame window
screenshot = pygame.transform.scale(screenshot, (width // div, height // div))

# Display screenshot at top of Pygame window
screen.blit(screenshot, (0, 0))

# Define colors
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)

# Define circles and line
orange_circle_toggled_on = False
blue_circle_toggled_on = False

orange_circle_pos = [0, 0]
blue_circle_pos = [0, 0]

def resetfile():
    with open('macro.py','w') as macro:
        prep = """import adbcontroller as adbc
from time import sleep
adbc.connect()
#this is where the macro starts
"""
        macro.write(prep)


def write_output(content):
    with open('macro.py', 'a') as file:
        file.write(content+"\n")

def gui():
    global orange_circle_pos
    global orange_circle_toggled_on
    global blue_circle_pos
    global blue_circle_toggled_on
    def mode_selected():
        if mode_selector.value == "swipe/tap":
            info_text.value = "text box as delay\nswipe: if 2 circles are on pygame screen (orange and blue)\n it swipes blue->orange\ntap: if 1 is present taps on that one\nlong press: just put the 2 in the same position"
        elif mode_selector.value == "text":
            info_text.value = "types the text thru adb, not really sure how it works yet"
        elif mode_selector.value == "keycode":
            info_text.value = "custom keycode for adb, takes it from textbox"
        elif mode_selector.value == "custom":
            info_text.value = "runs any system command from textbox"
        elif mode_selector.value == "delay":
            info_text.value = "Should be simple, its just a delay,\n type a number in and place confirm,\n or set it to something specific\nso you can go back and edit it into something random."


    def confirm():
        global orange_circle_toggled_on
        global orange_circle_pos
        global blue_circle_toggled_on
        global blue_circle_pos
        if mode_selector.value == "swipe/tap":
            if blue_circle_toggled_on and orange_circle_toggled_on:
                try:
                    delay = int(extra_text_box.value)
                except:
                    extra_text_box.value = 1000
                    delay = extra_text_box.value
                write_output(f"adbc.swipe(\"{blue_circle_pos[0]} {blue_circle_pos[1]} {orange_circle_pos[0]} {orange_circle_pos[1]} {delay}\")")
            elif blue_circle_toggled_on:
                write_output(f"adbc.tap(\"{blue_circle_pos[0]} {blue_circle_pos[1]}\")")
            elif orange_circle_toggled_on:
                write_output(f"adbc.tap(\"{orange_circle_pos[0]} {orange_circle_pos[1]}\")")
        elif mode_selector.value == "text":
            write_output(f'adbc.text(\"{extra_text_box.value}\")')
        elif mode_selector.value == "keycode":
            write_output(f'adbc.keycode(\"{extra_text_box.value}\")')
        elif mode_selector.value == "custom":
            write_output(f'adbc.write_to_console(\"{extra_text_box.value}\")')
        elif mode_selector == "delay":
            try:
                float(extra_text_box.value)
            except:
                pass
            else:
                write_output(f'time.sleep({extra_text_box.value})')


                
        


    app = App(title="Mode Selector")

    mode_list = ["swipe/tap", "text", "keycode", "custom", "delay"]
    mode_selector = Combo(app, options=mode_list, command=mode_selected)

    info_text = Text(app, text="")
    info_text.value = "text box as delay\nswipe: if 2 circles are on pygame screen (orange and blue)\n it swipes blue->orange\ntap: if 1 is present taps on that one\nlong press: just put the 2 in the same position"

    extra_text_box = TextBox(app, text="")
    extra_text_box.show()

    confirm_button = PushButton(app, text="Confirm", command=confirm)
    reset_button = PushButton(app, text="Reset macro.py", command=resetfile)

    app.display()

zero = threading.Thread(target=gui)
zero.start()



counter = 0
while True:
    counter += 1
    if counter % 10 == 0:
        screenshot = pygame.image.load('screenshot.png')
        screenshot = pygame.transform.scale(screenshot, (width // div, height // div))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Check if right click is pressed
            if event.button == 3:
                orange_circle_toggled_on = not orange_circle_toggled_on
                # Set orange circle position to mouse position when toggled on
                if orange_circle_toggled_on:
                    orange_circle_pos = mouse_pos
            # Check if left click is pressed
            elif event.button == 1:
                blue_circle_toggled_on = not blue_circle_toggled_on

                # Set blue circle position to mouse position when toggled on
                if blue_circle_toggled_on:
                    blue_circle_pos = mouse_pos


    # Draw screenshot on screen again to clear previous circles and line
    screen.blit(screenshot, (0, 0))

        # Draw orange circle if toggled on by right click
    if orange_circle_toggled_on:
            pygame.draw.circle(screen, ORANGE, orange_circle_pos, 10, 2)

        # Draw blue circle if toggled on by left click
    if blue_circle_toggled_on:
            pygame.draw.circle(screen, BLUE, blue_circle_pos, 10, 2)

        # Draw line between both circles if both are toggled on
    if blue_circle_toggled_on and orange_circle_toggled_on:
        pygame.draw.line(screen, (255, 255, 255), orange_circle_pos, blue_circle_pos, width=2)

        # Update display after drawing circles and line on it
    pygame.display.update()

