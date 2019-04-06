import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def test(self):

    
def setup(bot):
  bot.add_cog(Join(bot))
