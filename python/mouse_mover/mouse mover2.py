#to do: make non 9 position moving

from pydirectinput import move
from random import randint
FAILSAFE = False
try:
    value = open("movevalue.txt")
except:
    print("File not found: Please create a file called movevalue.txt")
try:
    m = float(value.read())
except:
    m = 1
    print("Loading config failed: loading 1 as the new value")
    
value.close()
while True:
    m = m+0.1
    mult = m//1
    value = open("movevalue.txt", "w")
    value.write(str(m))
    value.close
    print(mult,m)
    for i in range(50):
        
        move(int(((randint(1,3)-2)*mult)), int(((randint(1,3)-2)*mult)))
