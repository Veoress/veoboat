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
    await self.bot.say('Ahoj :D')
    return
  
  @command.command()
  async def ping(self):
    await self.bot.say('Ping: {0}'.format(round(self.bot.latency, 1)))
    return

    
def setup(bot):
  bot.add_cog(Cmds(bot))
