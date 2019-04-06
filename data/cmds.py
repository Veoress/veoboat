import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def test(self):
    await self.bot.say('test')

    
def setup(bot):
  bot.add_cog(Cmds(bot))
