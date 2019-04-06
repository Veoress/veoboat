import discord
from discord.ext import commands

class Commaner:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def load(self):
    await self.bot.say('uložiště: **COMMANDS** bylo načteno')
    return

    
def setup(bot):
  bot.add_cog(Commander(bot))
