import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def help(self, ctx):
    
    embed=discord.Embed(title="**Help**", description="** **", color=0x54ce1a)
    embed.set_author(name=" ")
    embed.add_field(name="**4 |General:**", value="`ping, ahoj, help, userinfo `", inline=True)
    embed.add_field(name="**3 |Fun:**", value="`number, rdance, fortmap `", inline=True)
    embed.add_field(name="**2 |Bot:**", value="`number, rdance, fortmap `", inline=True)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    return

    
def setup(bot):
  bot.add_cog(Helper(bot))
