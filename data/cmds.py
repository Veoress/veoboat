import discord
import random
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def load(self):
    await self.bot.say('uložiště: **COMMANDS** nefaká')
    return
   
  @commands.command()
  async def ahoj(self):
    await self.bot.say('**no nazdar :D**')
    return

  @commands.command(pass_context=True)
  async def number(self, ctx):
    await self.bot.say("Práva byla odcizena xD")
    return

  @commands.command()
  async def ping(self):
    await self.bot.say('nefaká')
    return

  @commands.command()
  async def pgserver(self):
    await self.bot.say('PandaGaming Server: https://discord.gg/mNEhAJA \n tento command si klidně nechte xDDD') 
    return

def setup(bot):
  bot.add_cog(Cmds(bot))
