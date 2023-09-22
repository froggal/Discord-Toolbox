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
    await app.change_presence(status=discord.Status.online, activity=discord.Game(f"$도움말, {str(len(app.guilds))}개의 서버에서 작동 중"))

@app.command()
async def 도움말(ctx):
    await ctx.reply(embed=embed("도움말", "도움말은 여기서 확인해주세요! \n https://keyfrog.notion.site/3b2ac8d6f257421d82601e22ab7ddbde?v=85a5afa584864c11affd4dc97c5230ca&pvs=4"))

@app.command()
async def 덧셈(ctx, a: int, b: int):
    await ctx.reply(embed=embed('덧셈', f'{a} + {b} = {a + b}'))

@app.command()
async def 뺄셈(ctx, a: int, b: int):
    await ctx.reply(embed=embed('뺄셈', f'{a} - {b} = {a - b}'))

@app.command()
async def 곱셈(ctx, a: int, b: int):
    await ctx.reply(embed=embed('곱셈', f'{a} X {b} = {a * b}'))

@app.command()
async def 나눗셈(ctx, a: int, b: int):
    await ctx.reply(embed=embed('나눗셈', f'{a} / {b} = {a / b}'))

@app.command()
async def 주사위(ctx):
    await ctx.reply(
        embed=embed('🎲 주사위', f'숫자는 {random.randrange(1, 6)}이예요!')
    )



app.run()