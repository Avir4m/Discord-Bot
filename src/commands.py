from discord.ext import commands
import requests

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        result = requests.get("https://meme-api.herokuapp.com/gimme").json()
        await ctx.send(result["url"])


async def setup(bot):
    await bot.add_cog(commands(bot))