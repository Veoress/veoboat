import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    await self.bot.say('userinfo command je v modu nastavování')
    return

    
def setup(bot):
  bot.add_cog(Userinfo(bot))
