import discord
import asyncio
from discord.ext import commands

from func import get_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = ".", intents=intents)
discord.utils.setup_logging() # Enables logging

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} - Version: {discord.__version__}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



async def main():
    async with bot:
        # loads extension commands
        await bot.load_extension('cogs.commands')
        await bot.load_extension('cogs.voice')
        await bot.start(get_token()) # starts the server


asyncio.run(main())