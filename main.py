# Import the correct code.
import discord 
from discord.ext import commands
from discord import ui
from mimetypes import init
from discord.ext.commands import Context
from dotenv import load_dotenv
import os

# Thingies :3
load_dotenv('token.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


# Intents
intents = discord.Intents.all() 
intents.message_content = True
client = discord.Client(intents=intents)

### The below code is intended for Ginger's Home.
### Please refer to the GitHub page for more information.

# Sends out a start signal to alert that the bot is ready to go.
@client.event
async def on_ready():
    status_channel = client.get_channel(1323516719402061844)
    await status_channel.send("Bot Start, running on `fedora`.")

# Sends out a welcome message when a new member joins.
@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel(1323516642839367711)
    await welcome_channel.send(f"Hello, {member.mention}! We welcome you to Ginger's Home.")

# YOU BETTER NOT SHARE THIS FUCKING TOKEN OR I WILL END YOU
client.run(DISCORD_TOKEN)
