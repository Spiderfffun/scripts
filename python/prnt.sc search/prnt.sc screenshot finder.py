from pyautogui import *
import random
import keyboard
import time
values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
howmuch = int(input("Please enter the amount of pictures the program will take: "))
time.sleep(5)
screens = 0
x = 0
trying = 0
while x == 0:
    if not keyboard.is_pressed("F9"):
        moveTo(224,56,0.1)
        a = random.choice(values)
        b = random.choice(values)
        c = random.choice(values)
        d = random.choice(values)
        click()
        write("https://prnt.sc/")
        write(a+b+c+d)
        press("enter")
        time.sleep(0.85)
        trying = trying + 1
        if pixel(646, 215) == (0,0,0):
            print("not found ",a+b+c+d, trying)
        else:
            testforimage = locateOnScreen("E:\Lun\py\\browse.png")
            print(testforimage)
            if testforimage == None:
                print("found image")
                screenshot(str("screenshots/"+a+b+c+d+".png"))
                screens = screens + 1
                if screens > howmuch-1:
                    print("Finished taking",howmuch,"screenshots")
                    stop = input("press enter to continue")
                    time.sleep(3)
            else:
                print("found not",a+b+c+d,trying)
    else:
        print("F9 held, stopping program until continued\n")
        stop = input("Press enter to continue the program (after 3 seconds)")
        time.sleep(3)
