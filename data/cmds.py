import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def ping(self):
    await self.bot.say('pong')
    return
  
  @command.command(pass_context=True)
  async def userinfo(ctx, user: discord.Member=None):
    if not user:
      user = ctx.message.author

    embed=discord.Embed(title="JMÉNO", description=" {} ".format(user.mention), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="STATUS", value=" {} ".format(user.status), inline=True)
    embed.add_field(name="NEJVĚTŠÍ ROLE", value=" {} ".format(user.top_role.mention), inline=True)
    embed.add_field(name="PŘIPOJIL SE", value=" {} ".format(user.joined_at.strftime(" %d %n %Y  %k:%M:%S ")), inline=False)
    embed.add_field(name="ID", value=" {} ".format(user.id), inline=False)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    reutn

    
def setup(bot):
  bot.add_cog(Cmds(bot))