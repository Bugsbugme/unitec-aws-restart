import os

import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTAzNzQ4MTE1NzEyMzY0OTU0Nw.Gs8WWS.Dn04RJDDJ8mv-nVLY344A8ttv96Va7Znsilbl4"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced: {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(context):
    await context.response.send_message(f"Hi {context.user.mention}", ephemeral=True)


@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="The thing to say")
async def say(context, thing_to_say: str):
    await context.response.send_message(f"{context.user.name} said `{thing_to_say}`")


@bot.tree.command(name="github")
async def github(context: discord.Interaction):
    await context.response.send_message("https://github.com/kris-classes/restart")


@bot.tree.command(name="ping")
async def ping(ctx):
    await ctx.response.send_message("pong", ephemeral=True)


@bot.tree.command(name="wave")
async def wave(ctx):
    await ctx.response.send_message(":wave:")


@bot.tree.command(name="youtube")
@app_commands.describe(url="The youtube url")
async def youtube(ctx, url: str):
    os.system(f"yt-dlp {url}")
    await ctx.responsse.send.message("Downloading video...")


bot.run(TOKEN)
