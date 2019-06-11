import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def help(self):
    embed=discord.Embed(title="**Help**", description="** **", color=0x54ce1a)
    embed.set_author(name=" ")
    embed.add_field(name="**4 |General:**", value="`ping, ahoj, help, userinfo `", inline=False)
    embed.add_field(name="**3 |Fun:**", value="`number, rdance, fortmap `", inline=False)
    await self.bot.say(embed=embed)
    return

    
def setup(bot):
  bot.add_cog(Helper(bot))
