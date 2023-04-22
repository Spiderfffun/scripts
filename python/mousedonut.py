import win32api
import time
from pywintypes import error
from pyautogui import size

width, height = size()

def move_mouse():
    x, y = win32api.GetCursorPos()
    try:
        if x == 0:
            win32api.SetCursorPos((width - 2, y))
        elif x == width - 1:
            win32api.SetCursorPos((1, y))
        elif y == 0:
            win32api.SetCursorPos((x, height - 2))
        elif y == height - 1:
            win32api.SetCursorPos((x, 1))
    except error:
        pass

while True:
    move_mouse()
    time.sleep(0.01)