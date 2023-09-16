import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
app = commands.Bot(command_prefix='$', intents=intents)
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


@app.event
async def on_ready():
    print('Connected to Discord')
    await app.change_presence(status=discord.Status.online, activity=discord.Game("$도움말"))

@app.command()
async def 도움말(ctx):
    await ctx.reply(embed=embed("도움말", "도움말은 여기서 확인해주세요!"))



app.run(os.getenv("DICOTOKEN"))