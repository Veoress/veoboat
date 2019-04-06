import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
  @command.command(pass_context=True)
  async def userinfo(self):
    await self.bot.say("test userinfo repository")
    return

    
def setup(bot):
  bot.add_cog(Userinfo(bot))
