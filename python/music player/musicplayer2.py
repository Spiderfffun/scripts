#To do:
#   Make images for all the buttons.


from just_playback import Playback
import os
from time import sleep
from random import choice
import keyboard
from guizero import App, Box, PushButton, Slider, CheckBox, Text, ListBox
playback = Playback()

def setclick():
    if volume.visible:
        volume.hide()
        random.hide()
        loopone.hide()
        rmv.hide()
    else:
        loopone.show()
        volume.show()
        random.show()
        rmv.show()
        
def vol(value):
    playback.set_volume(int(value)/100)

def pp():
    if pp.text == "pause":
        playback.pause()
        pp.text = "play"
    else:
        playback.resume()
        pp.text = "pause"

def rng(music):
    song = choice(music)

def repeat1s():
    after(500, repeat1s, args=None)
    if not playback.active and not pp.text == "play":
        time.value = str(playback.curr_pos//60) + ":" + str(playback.curr_pos%60) + " / " + str(playback.duration//60) + ":" + str(playback.duration%60)
        nxt()
    
def loop():
    if playback.loops_at_end:
        playback.loop_at_end(False)
    else:
        playback.loop_at_end(True)

def fwd():
    cur = playback.curr_pos
    playback.seek(cur+5)

def bkw():
    cur = playback.curr_pos
    playback.seek(cur-5)

def nxt():
    songz = songs.items
    #print(songz) debug
    if random.value:
        if rmv.value:
            song = choice(songz)
            current.value = song
            playback.load_file(song)
            if pp.text == "pause":
                playback.play()
            songz.remove(song)
            songs.items = songz
        else:
            song = choice(songz)
            current.value = song
            playback.load_file(song)
            if pp.text == "pause":
                playback.play()
    else:
        if rmv.value:
            song = songz[0]
            current.value = song
            playback.load_file(song)
            if pp.text == "pause":
                playback.play()
            songz.remove(song)
            songs.items = songz
        else:
            #try:
            text = songnumb.value
            number = int(text)
            song = songz[number] 
            current.value = song
            songnumb.value = str(int(songnumb.value)+1)
            playback.load_file(song)
            if pp.text == "pause":
                playback.play()
    print(current.value)
def prv():
    song.previous

playback = Playback()

filename = os.path.basename(__file__)
#print(filename) debug
music = os.listdir()
#print(music)
music.remove(filename)
try:
    music.remove("playerconfig.txt")
except:
    print("config didn't load correctly.")
#print(music,"\n\n") debug

current = "None"



app = App(bg = (20,20,20),title="Pyplayer")

player_box = Box(app, width="fill", align="bottom")
top_box = Box(app, width="fill", align="top")
pp = PushButton(player_box, text="play", command=pp)
Next = PushButton(player_box, text=">>", align="right", command = nxt)
Previous = PushButton(player_box, text="<<", align="left",command=prv)
fd = PushButton(player_box, text=">", align="right", command=fwd)
bk = PushButton(player_box, text="<", align="left", command=bkw)
settings = PushButton(top_box, image="settings.png", align="left", width=50, height=50, command=setclick)
volume = Slider(app, visible= False, command = vol)
random = CheckBox(app, visible= False,text="Do random songs?", command = rng, args= [music])
loopone = CheckBox(app, visible= False,text="Loop single song?", command = loop)
rmv = CheckBox(app, visible= False,text="Remove songs after play?")
current = Text(player_box,visible= True, text=current)
songs = ListBox(app,visible= False, items=music)
songnumb = Text(app,visible= False, text="0")
prev = Text(player_box,visible= False, text=current)
time = Text(player_box,visible= True, text=current)


pp.text_color = "blue"
Next.text_color = "blue"
Previous.text_color = "blue"
fd.text_color = "blue"
bk.text_color = "blue"
volume.text_color = "blue"
random.text_color = "blue"
loopone.text_color = "blue"
rmv.text_color = "blue"
current.text_color = "blue"
time.text_color = "blue"



nxt()
playback.pause()














app.display()
