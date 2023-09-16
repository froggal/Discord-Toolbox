import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
app = commands.Bot(command_prefix='$', intents=intents)

@app.event
async def on_ready():
    print('Connected to Discord')
    await app.change_presence(status=discord.Status.online, activity=discord.Game("$도움말"))

@app.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요")

app.run(os.getenv("DICOTOKEN"))