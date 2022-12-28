import disnake
from disnake.ext import commands

class Test_cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'start {self.bot.user}')

def setup(bot):
    bot.add_cog(Test_cmd(bot))
