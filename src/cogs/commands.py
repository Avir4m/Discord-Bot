from discord.ext import commands
import discord
import requests

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        meme = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed()
        embed.set_image(url=meme["url"])
        embed.add_field(name="Original Post", value=meme["postLink"], inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def reverse(self, ctx, arg):
        number = int(arg)
        first_digit = int(number / 10)
        second_digit = number % 10 * 10
        await ctx.send(first_digit + second_digit)

    @commands.command()
    async def math(self, ctx):

        problem = requests.get("https://x-math.herokuapp.com/api/random?max=15&negative=1").json()
        answer = problem["answer"]
        await ctx.send(problem["expression"])

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