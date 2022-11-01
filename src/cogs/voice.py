from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self, ctx):
        if not ctx.voice_client:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("The bot is already connected to a voice channel.")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            user_channel = ctx.author.voice.channel
            bot_channel = ctx.voice_client.channel
            if user_channel == bot_channel:
                await ctx.guild.voice_client.disconnect()
            else:
                await ctx.send("You are not in the same voice channel as the bot.")
        else:
            await ctx.send("The bot is not in any voice channel")

async def setup(bot):
    await bot.add_cog(voice(bot))