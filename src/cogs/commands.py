from discord.ext import commands
from discord import app_commands
import discord
import requests

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="meme", description="Sends random meme")
    async def meme(self, ctx):
        meme = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed()
        embed.set_image(url=meme["url"])
        embed.add_field(name="Original Post", value=meme["postLink"], inline=True)
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="math", description="Sends random math expression for you to solve")
    async def math(self, ctx):

        problem = requests.get("https://x-math.herokuapp.com/api/random?max=15&negative=1").json()
        answer = problem["answer"]
        await ctx.response.send_message(problem["expression"])

        def check(m):
            return len(m.content) >= 1 and m.author != self.bot.user
            
        ALLOWED_TRIES = 3
        a = 0

        while a <= ALLOWED_TRIES:
            user_answer = await self.bot.wait_for("message", check=check)
            if int(user_answer.content) == int(answer):
                await ctx.send("Your answer is correct!")
                break
            else:
                await ctx.send(f"Your answer is wrong, you have {ALLOWED_TRIES-a} tries left.")
                a += 1

async def setup(bot):
    await bot.add_cog(commands(bot))