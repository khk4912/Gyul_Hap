import discord
from discord.ext import commands
import random
import asyncio


async def check_owner(ctx):
    owner = [119550317003014144, 289729741387202560,
             420919892636598272, 265003834521157633]
    if ctx.author.id in owner:
        return True
    else:
        await ctx.send("님 ㄴㄱ?")


class Gyul(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.on_load())
        self.gyulDict = {}

    async def on_load(self):
        await self.bot.wait_until_ready()
        guild = self.bot.get_guild(669584475633745921)
        gyulDict = dict()
        for i in guild.emojis:
            gyulDict[i.name] = '<:{}:{}>'.format(i.name, i.id)
        self.gyulDict = gyulDict
        return True

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send(self.gyulDict)

    @commands.command(name='리로드')
    @commands.check(check_owner)
    async def reload(self, ctx, module):
        try:
            self.bot.reload_extension(module)
            await ctx.send("✅")
        except:
            await ctx.send("⚠️")

    @commands.command(name='랜덤')
    async def board_random(self, ctx):
        values = list(self.gyulDict.values())
        x = random.sample(values, 9)
        gameBoard = [x[0:3], x[3:6], x[5:8]]
        await ctx.send(gameBoard)


def setup(bot):
    bot.add_cog(Gyul(bot))
