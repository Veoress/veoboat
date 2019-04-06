import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def userinfo(self, ctx, user: discord.Member=None):
    if not user:
      user = ctx.message.author
      
    embed=discord.Embed(title="test", description=" {} ".format(user.mention), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="** **", value="** **", inline=True)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    await self.bot.say('userinfo command je v modu nastavování')
    return

    
def setup(bot):
  bot.add_cog(Userinfo(bot))
