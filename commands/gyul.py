import discord
from discord.ext import commands


class Gyul(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.emojis = {}

    @commands.command(name='테스트')
    async def test(self, ctx):
        await ctx.send([str(i) for i in ctx.guild.emojis])


def setup(bot):
    bot.add_cog(Gyul(bot))
