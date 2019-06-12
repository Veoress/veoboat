import discord
import random
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

  @commands.command(pass_context=True)
  async def number(self, ctx):
    await self.bot.say(random.randint(1,100))
    return

    
def setup(bot):
  bot.add_cog(Cmds(bot))
