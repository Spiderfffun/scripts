import pydirectinput as pyautogui
import random
pyautogui.FAILSAFE = False
value = open("movevalue.txt")
m = float(value.read())
value.close()
while True:
    m = m+0.1
    mult = m//1
    value = open("movevalue.txt", "w")
    value.write(str(m))
    value.close
    print(mult,m)
    for i in range(50):
        
        pyautogui.move(int(((random.randint(1,3)-2)*mult)), int(((random.randint(1,3)-2)*mult)))
