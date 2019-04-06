import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def load(self):
    await self.bot.say('uložiště: **COMMANDS** bylo načteno')
    return
  
  @commands.command()
  async def ahoj(self):
    await self.bot.say('**Ahoj :D**')
    return
  
  @commands.command()
  async def ping(self):
    await self.bot.say('**ping:** {} ms'.format(self.bot.latency))
    return

    
def setup(bot):
  bot.add_cog(Cmds(bot))
