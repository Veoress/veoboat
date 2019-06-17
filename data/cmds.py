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

  @commands.command()
  async def ping(self):
    await self.bot.say('Pong!')
    return


  @commands.command()
  async def help(self):
    embed=discord.Embed(title="**PandaGaming Server**", description="** **", color=0x54ce1a)
    embed.set_author(name=" ")
    embed.add_field(name="**Invite:**", value="`https://discord.gg/mNEhAJA`", inline=False)
    await self.bot.say(embed=embed)
    return

def setup(bot):
  bot.add_cog(Cmds(bot))
