import subprocess #fun fact these 3 lines are the only code that isn't spighetti
import cv2
import numpy as np

def connect(port = input("What port is adb running on? ")):
    subprocess.run(['adb','disconnect'])
    command = f"adb connect localhost:{port}"
    subprocess.run(command.split())

def take_screenshot(name='screenshot'):
    subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])
    subprocess.run(["adb", "pull", "/sdcard/screenshot.png", f"{name}.png"])

def write_to_console(command):
    subprocess.run(command.split())

def find_image(image_to_recognize):
    where_to_try_to_recognize_it = 'screenshot.png'
    image_to_recognize = "recognition\\" + image_to_recognize
    img = cv2.imread(where_to_try_to_recognize_it)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image_to_recognize, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return True, max_loc
    else:
        return False, None
    
def swipe(args):
    write_to_console("adb shell input swipe " + args)

def tap(args):
    write_to_console("adb shell input tap " + args)

def text(args):
    write_to_console("adb shell input text " + args)

def keycode(args):
    write_to_console("adb shell input keycode " + args)

if __name__ == '__main__':
    connect()
    take_screenshot()
    print(find_image('playstore.png'))
    while 1:
        cmd = input("command: adb ")
        write_to_console("adb "+cmd)