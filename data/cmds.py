import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def load(self):
    await self.bot.say('**test Help 4 |General:**   `ping, ahoj, help, userinfo `')
    await self.bot.say('**test Help 3 |Fun:**  `number, rdance, fortmap `')
    await self.bot.say('**test Help 2 |Bot:**  `invite, veo_server `')
    return

    
def setup(bot):
  bot.add_cog(Cmds(bot))
