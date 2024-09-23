import discord
import requests
import os
from discord.ext import commands
from decouple import config
from colorama import Fore, Style

# Reading from .env
infectpre = config('prefix')
bot_token = config('token')
authorized_user = int(config('userid'))

# Bot Setup
bot = commands.Bot(command_prefix=infectpre, self_bot=True, help_command=None)

# Authorization decorator
def infected():
    def predicate(ctx):
        return ctx.author.id == authorized_user
    return commands.check(predicate)

# Function to make API request
def make_api_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# NSFW Waifu.Pics API Commands
@bot.command()
@commands.is_nsfw()
async def waifunsfw(ctx):
    url = "https://api.waifu.pics/nsfw/waifu"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No NSFW waifu image found.")

@bot.command()
@commands.is_nsfw()
async def nekonsfw(ctx, times: int = 1):
    url = "https://api.waifu.pics/nsfw/neko"  # NSFW neko images
    for _ in range(times):
        data = make_api_request(url)
        if data and 'url' in data:
            await ctx.send(data['url'])
        else:
            await ctx.send("No NSFW neko image found.")

@bot.command()
@commands.is_nsfw()
async def trap(ctx):
    url = "https://api.waifu.pics/nsfw/trap"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No NSFW trap image found.")

@bot.command()
@commands.is_nsfw()
async def blowjob(ctx):
    url = "https://api.waifu.pics/nsfw/blowjob"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No NSFW blowjob image found.")

# SFW Waifu.Pics API Commands
@bot.command()
async def waifusfw(ctx):
    url = "https://api.waifu.pics/sfw/waifu"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No SFW waifu image found.")

@bot.command()
async def nekosfw(ctx):
    url = "https://api.waifu.pics/sfw/neko"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No SFW neko image found.")

@bot.command()
async def cuddle(ctx):
    url = "https://api.waifu.pics/sfw/cuddle"
    data = make_api_request(url)
    if data and 'url' in data:
        await ctx.send(data['url'])
    else:
        await ctx.send("No SFW cuddle image found.")

# General Help Command
@bot.command()
async def help(ctx):
    help_message = """
    **General Commands**:
    <:y_black_flame:824067447795482655> `!neko <times>`: Send multiple neko images
    <:y_black_flame:824067447795482655> `!ping`: Check bot latency
    <:y_black_flame:824067447795482655> `!afk`: Set AFK message

    Use `!help_nsfw` for NSFW commands.
    Use `!help_sfw` for SFW commands.
    """
    await ctx.send(help_message)

# NSFW Help Command
@bot.command()
async def help_nsfw(ctx):
    help_message = """
    **NSFW Commands**:
    <:hot_hentai_legs:1158056031839080498> `!waifunsfw`: NSFW waifu images
    <:hot_hentai_legs:1158056031839080498> `!nekonsfw <times>`: NSFW neko images (with optional repeat)
    <:hot_hentai_legs:1158056031839080498> `!trap`: NSFW trap images
    <:hot_hentai_legs:1158056031839080498> `!blowjob`: NSFW blowjob images
    """
    await ctx.send(help_message)

# SFW Help Command
@bot.command()
async def help_sfw(ctx):
    help_message = """
    **SFW Commands**:
    <:SoloLegends_pepeamorcito:853982172074737724> `!waifusfw`: SFW waifu images
    <:SoloLegends_pepeamorcito:853982172074737724> `!nekosfw`: SFW neko images
    <:SoloLegends_pepeamorcito:853982172074737724> `!cuddle`: SFW cuddle images
    """
    await ctx.send(help_message)

# ASCII Banner and Bot Info when ready
@bot.event
async def on_ready():
    infbanner = """
.___        _____              __    _________                  .___         ____ 
|   | _____/ ____\____   _____/  |_  \_   ___ \  ___________  __| _/ ___  __/_   |
|   |/    \   __\/ __ \_/ ___\   __\ /    \  \/ /  _ \_  __ \/ __ |  \  \/  /|   |
|   |   |  \  | \  ___/\  \___|  |   \     \___(  <_> )  | \/ /_/ |   >    < |   |
|___|___|  /__|  \___  >\___  >__|    \______  /\____/|__|  \____ |  /__/\_ \|___|
         \/          \/     \/               \/                  \/        \/             
"""
    print(Fore.RED + infbanner + Style.RESET_ALL)
    print(f"{'='*30}")
    print(f"        Logged in as: {bot.user.name}")
    print(f"        Selfbot ID: {bot.user.id}")
    print(f"{'='*30}\n")
    print("InfectCord is connected")
    print(f"{'-'*30}")
    print(f"   Username: {bot.user.name}")
    print(f"   Guilds: {len(bot.guilds)}")
    print(f"   Members: {sum([guild.member_count for guild in bot.guilds])}")
    print(f"{'-'*30}")
    print("Developer - I N F E C T E D")

# Cogs loader (if any cogs exist)
def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            bot.load_extension(f'cogs.{cog_name}')

# Run the bot
bot.run(bot_token, reconnect=True)
