import discord
from discord.ext import commands
import TOKEN
import logging


class Gyul_Hap(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=["!"]
        )

        for i in TOKEN.initial_extensions:
            self.load_extension(i)

    async def on_ready(self):
        print('=====')
        print(self.user.name, '레디드')
        print('=====')

    async def on_message(self, message):
        await self.process_commands(message)


bot = Gyul_Hap()
bot.run(TOKEN.bot_token)
