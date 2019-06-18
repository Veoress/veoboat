import discord
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
    await self.bot.say('**Ahoj :D**')
    return

  @commands.command(pass_context=True)
  async def number(self):
    await self.bot.say(random.randit(1,100)
    return

  @commands.command()
  async def ping(self):
    await self.bot.say('Pong!')
    return

  @commands.command()
  async def pgserver(self):
    await self.bot.say('PandaGaming Server: https://discord.gg/mNEhAJA') 
    return

def setup(bot):
  bot.add_cog(Cmds(bot))
