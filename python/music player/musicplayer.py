from just_playback import Playback
import os
from time import sleep
from random import choice
import keyboard

playback = Playback()

def q(q):
    q = q + " Y/N\n"
    answer = input(q)
    if answer == ("y" or "Y" or "yes" or "Yes" or "YES"):
        return 1
    else:
        return 0
    
filename = os.path.basename(__file__)
print(filename)
music = os.listdir()
print(music)
music.remove(filename)
try:
    music.remove("playerconfig.txt")
except:
    print("config didn't load correctly.")
print(music,"\n\n")
config = q("Recreate config?")

random = q("Should songs be random?(if no, played alphabetically)")

replayable = q("Should songs be replayable?")

if config:
    print("not ready yet")
    #make load config


if not replayable:
    if not random:
        for i in music:
            print("Playing",i,"\nSongs remaining:", len(music))
            playback.load_file(i)
            playback.play()
            while playback.active:
                if keyboard.is_pressed("F9") and playback.playing:
                    playback.pause()
                elif keyboard.is_pressed("F9") and not playback.playing:
                    playback.resume()
                sleep(1)
    else:
        for i in music:
            song = choice(music)
            music.remove(song)
            print("Playing", song,"\nSongs remaining:", len(music))
            playback.load_file(song)
            playback.play()
            while playback.active:
                if keyboard.is_pressed("F9") and playback.playing:
                    playback.pause()
                elif keyboard.is_pressed("F9") and not playback.playing:
                    playback.resume()
                sleep(1)
else:
    if not random:
        while 1:
            for i in music:
                print("Playing",i,"\nSongs remaining until reset:", len(music))
                playback.load_file(i)
                playback.play()
                while playback.active:
                    if keyboard.is_pressed("F9") and playback.playing:
                        playback.pause()
                    elif keyboard.is_pressed("F9") and not playback.playing:
                        playback.resume()
                    sleep(1)
    else:
        for i in music:
            song = choice(music)
            print("Playing", song)
            playback.load_file(song)
            playback.play()
            while playback.active:
                if keyboard.is_pressed("F9") and playback.playing:
                    playback.pause()
                elif keyboard.is_pressed("F9") and not playback.playing:
                    playback.resume()
                sleep(1)
