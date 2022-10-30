#to do: circle move

print("To stop the program if it gets out of control,\nalt + tab to it and use alt f4 on it.\n")

from pydirectinput import move
import pydirectinput
from random import randint
print(r"Do you want to use failsafe Y\N?")
print("(Not recommended, because the program crashes when the mouse is in the corner.)")
usesafe = input()

pydirectinput.FAILSAFE = False
try:
    value = open("movevalue.txt")
except:
    print("File not found: Please create a file called movevalue.txt\n")
try:
    m = float(value.read())
except:
    m = 1
    print("Loading config failed: loading 1 as the new value\n")
    
    value.close()

mode = input("Please enter the mode: \n TR for true random \n R for normal (9 position) random \n SQR for moving the mouse in a square\n")
if mode == "TR" or mode == "tr" or mode == "Tr" or mode == "TR" or mode == "tr" or mode == "Tr":
    increase = input("Do you want the mouse moving to increase over time? Y/N \n")
    if increase == "y" or increase == "Y":
        if mode == "TR" or mode == "tr" or mode == "Tr":
            print("Moving in true (new) random")
            while True:
                m = m+0.1
                mult = m//1
                value = open("movevalue.txt", "w")
                value.write(str(m))
                value.close()
                print(mult,m)
                for i in range(50):
                    move(int((((randint(100,300)-200)*mult)//100)), int((((randint(100,300)-200)*mult)//100)))

        elif mode == "R" or mode == "r":
            print("Moving in normal (old) random mode")
            while True:
                m = m+0.1
                mult = m//1
                value = open("movevalue.txt", "w")
                value.write(str(m))
                value.close()
                print(mult,m)
                for i in range(50):
                    move(int((((randint(1,3)-2)*mult)//1)), int((((randint(1,3)-2)*mult)//1)))
    else:
        mult = m//1
        print(mult,m)
        if mode == "TR" or mode == "tr" or mode == "Tr":
            print("Moving in true (new) random")
            while True:
                move(int((((randint(100,300)-200)*mult)//100)), int((((randint(100,300)-200)*mult)//100)))

        elif mode == "R" or mode == "r":
            print("Moving in normal (old) random mode")
            while True:
                move(int((((randint(1,3)-2)*mult)//1)), int((((randint(1,3)-2)*mult)//1)))

else:
    if mode == "SQR" or mode == "sqr" or mode == "Sqr":
        pixels = int(input("Please input the pixels to move the cursor: "))
        print("Moving in a square by",pixels,"pixels")
        while True:
            move(pixels,0)
            move(0,pixels)
            move(-pixels,0)
            move(0,-pixels)
