import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    if not user:
      user = ctx.message.author
      
    embed=discord.Embed(title="**INFORMACE O UŽIVATELI**", description=" ", color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url="")
    embed.add_field(name="**TENTO COMMAND JE MOMENTÁLNĚ NEFUNKČNÍ**", value="** **", inline=False)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    return

    
def setup(bot):
  bot.add_cog(Userinfo(bot))
