import keyboard
import pyautogui as p
import time
x = 0
def spam():
    p.hotkey("ctrlleft", "v")
    p.typewrite(["enter"])


while x<1000:
    if keyboard.is_pressed('F9'):
        print("F9", x)
        spam()
        time.sleep(0.1)
        x = x+1
    
