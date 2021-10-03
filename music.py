import discord
import youtube_dl
from discord.ext import commands

class music(commands.Cog, name="Music"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a `Voice Channel`")
        voice_channel=ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

def setup(bot: commands.Bot):
    bot.add_cog(music(bot))