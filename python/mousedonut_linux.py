import Xlib.display
import time
from pyautogui import size

display = Xlib.display.Display()
screen = display.screen()
root = screen.root

width, height = size()

def move_mouse():
    x, y = root.query_pointer()._data["root_x"], root.query_pointer()._data["root_y"]
    try:
        if x == 0:
            root.warp_pointer(width - 2, y)
        elif x == width - 1:
            root.warp_pointer(1, y)
        elif y == 0:
            root.warp_pointer(x, height - 2)
        elif y == height - 1:
            root.warp_pointer(x, 1)
        display.sync()
    except Xlib.error.XError:
        pass
print("working")
while True:
    move_mouse()
    time.sleep(0.01)
