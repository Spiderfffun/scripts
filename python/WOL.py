import discord
import discord.ext
from wakeonlan import send_magic_packet
import os
import json

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

fileread = ""
# computerlist: dict = dict()

def update():
    # global computerlist
    # computerlist = dict()
    # if os.path.isfile("computers.txt"):
    #     with open("computers.txt", "r") as f:
    #         fileread = f.read().split("\n")
    #         for i in fileread:
    #             computerlist[i.split("|")[0]] = i.split("|")[1]

    # else:
    #     with open("computers.txt", "w") as f:
    #         f.write("example|example\n")
    with open("computers.txt", "a") as file:
        pass
    try:
        with open("computers.txt", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    return data

update()
@client.event
async def on_ready():
    await tree.sync()
    print("ready")

@tree.command(name="boot", description="Boot a specific computer. Use /computers to see the available ones")
async def boot(interaction: discord.Interaction, computer: str):
    try:
        response = send_magic_packet(update()[computer])
    except Exception as e:
        response = str(e)
    if response == computer:
        await interaction.response.send_message("not in the list, /computers please")
    else:
        await interaction.response.send_message(str(response))

@boot.autocomplete('computer')
async def boot_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> list[discord.app_commands.Choice[str]]:
    computers = list(update().keys())
    return [
        discord.app_commands.Choice(name=computer, value=computer)
        for computer in computers if current.lower() in computer.lower()
    ]

@tree.command(name="computers", description="what computers are there rn?")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message(update())

@tree.command(name="bootmac", description="Boot a specific computer thru the mac address. Use /computers to see the available ones")
async def boot(interaction: discord.Interaction, computer: str):
    try:
        response = send_magic_packet(computer.replace(":","."))
    except Exception as e:
        response = str(e)
    if response == computer:
        await interaction.response.send_message("not in the list, /computers please")
    else:
        await interaction.response.send_message(str(response))

@tree.command(name="remove", description="Remove a specific computer off the list.")
async def remove_computer(interaction:discord.Interaction, name: str):
    try:
        data = update()
        if name in data:
            del data[name]
            with open("computers.txt", "w") as file:
                json.dump(data, file, indent=4)
    except Exception as e:
        await interaction.response.send_message(str(e))
    else:
        await interaction.response.send_message("done if it was there")


@tree.command(name="add", description="Add a specific computer to the list.")
async def add_computer(interaction: discord.Interaction, name: str, mac: str):
    try:
        data = update()
        data[name] = {"mac": mac}
        with open("computers.txt", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        await interaction.response.send_message(str(e))
    else:
        await interaction.response.send_message("done if it was there")



client.run("ODM0ODc4NDI3MDM1MDc0NTkw.G-NCS7.GOu7p7WFCceNKePxS5uvA1Q2VCSn9d05kFkbkw")
