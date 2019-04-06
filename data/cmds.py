import discord
from discord.ext import commands

class Basic:
  def __init__(self, bot):
    self.bot = bot
    
  @command.command()
  async def load(self):
    await self.bot.say('uložiště **COMMANDS** bylo načteno')
    return

    
def setup(bot):
  bot.add_cog(Basic(bot))
