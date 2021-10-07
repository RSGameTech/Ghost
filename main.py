import discord
import jishaku
import json
import os
from discord.ext import commands
from discoutils import MinimalEmbedHelp
from dotenv import load_dotenv
from Util import colour

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="--",help_command=MinimalEmbedHelp(color=0x7289DA),case_insensitive=True,intents=intents)

load_dotenv()
'''#JSON Data
with open("JSON\\token.json", "r") as to:
    data = json.load(to)
    token = data["token"]'''

#BOT On Ready
@bot.event
async def on_ready():
    text=f"""╠════════════════════════════════════════╣
║BOT is Ready                            ║
╠════════════════════════════════════════╣
║BOT Name -> {bot.user.name}              ║
║BOT ID   -> {bot.user.id}          ║
╚════════════════════════════════════════╝"""
    channel = bot.get_channel(840984262458081292)
    embed = discord.Embed(
        description = f"Ghost is Online\nPing:- {round(bot.latency * 1000)}ms",
        color = colour.normal_colour
    )
    #await channel.send(embed=embed)
    print(text)

#BOT Owner ID
bot.owner_ids=[699566190842085439,730454267533459568,768009526942760980]

#Cogs Loading
file=[
    'music'
]
for ext in file:
    bot.load_extension(f'{ext}')

bot.load_extension("jishaku")
bot.run(os.getenv("token"))