from discord.ext import commands
import discord
import requests

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        result = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed()
        embed.set_image(url=result["url"])
        embed.add_field(name="Original Post", value=result["postLink"], inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(commands(bot))