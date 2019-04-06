import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def help(self):
    await self.bot.say('**4 |General:**   `ping, ahoj, help, userinfo `')
    await self.bot.say('**3 |Fun:**  `number, rdance, fortmap `')
    await self.bot.say('**2 |Bot:**  `invite, veo_server `')
    return

    
def setup(bot):
  bot.add_cog(Helper(bot))
