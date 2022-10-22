import asyncio
import discord
from discord.ext import commands

from func import get_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = ".", intents=intents)
discord.utils.setup_logging() # Enables logging

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} - {bot.user.id} Version: {discord.__version__}')


async def main():
    async with bot:
        await bot.load_extension('commands')
        await bot.start(get_token())

asyncio.run(main())