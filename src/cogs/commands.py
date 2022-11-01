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

    @commands.command()
    async def reverse(self, ctx, arg):
        number = int(arg)
        first_digit = int(number / 10)
        second_digit = number % 10 * 10
        await ctx.send(first_digit + second_digit)
        

async def setup(bot):
    await bot.add_cog(commands(bot))