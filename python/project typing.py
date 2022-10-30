#this is all confusing and old stuff, as i haven't commented this before


import turtle as t #libraries
from turtle import *


help = "Commands: / to start command (must be lowercase), \ to close it \n h - view help (this page) \n c - change background or pen color \n m - set a size multiplier"
command = False #default values
m = 1 #multiplier
t.up()
t.listen()
x = 0


print(help)
inputs = input("") #input
pensize(3)

while x != 100:
    for i in inputs:
        if command == False:
            if i == "/": #check for command
                command = True
                print(" /  - Command mode activated")
            elif i == "0": #all numbers to write
                down()
                right(90)
                fd(100*m)
                left(90)
                fd(50*m)
                left(90)
                fd(100*m)
                left(90)
                fd(50*m)
                left(180)
                up()
                fd(100*m)
            elif i == "1":
                right(90)
                down()
                fd(100*m)
                right(180)
                fd(100*m)
                right(90)
                up()
                fd(50*m)
            elif i == "2":
                down()
                fd(50*m)
                right(90)
                fd(50*m)
                right(90)
                fd(50*m)
                left(90)
                fd(50*m)
                left(90)
                fd(50*m)
                up()
                left(90)
                fd(100*m)
                right(90)
                fd(50*m)
            elif i == "3":
                down()
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                lt(90)
                up()
                fd(50*m)
                lt(90)
                down()
                fd(50*m)
                lt(90)
                fd(100*m)
                rt(90)
                up()
                fd(50*m)
            elif i == "4":
                down()
                rt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(180)
                fd(100*m)
                up()
                rt(90)
                fd(50*m)
            elif i == "5":
                fd(50*m)
                down()
                rt(180)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                up()
                rt(90)
                fd(100*m)
                rt(90)
                fd(100*m)
            elif i == "6":
                rt(90)
                fd(50*m)
                down()
                lt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(100*m)
                rt(90)
                fd(50*m)
                up()
                fd(50*m)
            elif i == "7":
                down()
                fd(50*m)
                rt(90)
                fd(100*m)
                rt(180)
                up()
                fd(100*m)
                rt(90)
                fd(50*m)
            elif i == "8":
                down()
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                rt(90)
                fd(50*m)
                up()
                fd(50*m)
            elif i == "9":
                rt(90)
                fd(100*m)
                down()
                lt(90)
                fd(50*m)
                lt(90)
                fd(100*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                fd(50*m)
                lt(90)
                up()
                fd(50*m)
                rt(90)
                fd(50*m)
            elif i == " ":
                fd(50*m)
            elif i == "=":
                rt(90)
                
            elif i == "^":
                fd(50*m)
            elif i == "<":
                lt(90)
            elif i == ">":
                rt(90)
        if command:
            if i + " " == "\ ":
                command = False
                print(" \ - Command mode deactivated") #help menu down here \|/
            elif i == "c":
                colors = int(input("\"C\" - Change colors\n 1 - background \n 2 - pen \n"))
                if colors == 2:
                    t.color(input("Please enter the pen color:"))
                elif colors == 1:
                    t.bgcolor(input("Please enter the background color:"))
            elif i == "h":
                print(help)
            elif i == "m":
                m = float(input("Please enter a size multiplier: "))


    inputs = input() #redo input
    x = x + 1
