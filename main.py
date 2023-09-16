import os
import discord
from discord.ext import commands
import random
from baekjoon import boj
from baekjoon import solvedac
from baekjoon import problem

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

@app.command()
async def 사칙연산(ctx, type, left: int, right: int):
    if type == '덧셈':
        data = left + right
        await ctx.reply(
            embed=embed('사칙연산 - 덧셈', f'{left}+{right} = {data}'))
    elif type == '뺄셈':
        data = left - right
        await ctx.reply(
            embed=embed('사칙연산 - 뺄셈', f'{left}-{right} = {data}'))
    elif type == '곱셈':
        data = left * right
        await ctx.reply(
            embed=embed('사칙연산 - 곱셈', f'{left}X{right} = {data}'))
    elif type == '나눗셈':
        data = left / right
        await ctx.reply(
            embed=embed('사칙연산 - 나눗셈', f'{left}/{right} = {data}'))

app.run(os.getenv("DICOTOKEN"))