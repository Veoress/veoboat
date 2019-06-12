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
    
  @commands.command(pass_context=True)
  async def fortmap(self, ctx):
    embed=discord.Embed(title=" ", description=" ", color=0xb51ea9)
    embed.set_author(name=" ")
    embed.set_image(url="https://media.deseretdigital.com/file/8d92395855?resize=width_1200&type=jpg&c=6&a=e0717f4c")
    embed.add_field(name="**Fortnite Map**", value="** **", inline=True)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    return


@commands.command(pass_context=True)
  async def fortmap(self, ctx):
    embed=discord.Embed(title=" ", description=" ", color=0xb51ea9)
    embed.set_author(name=" ")
    embed.set_image(url="https://images.app.goo.gl/tn9jbMAxrdqjARd4A") 
    embed.add_field(name="**Rainbow Dance**", value="** **", inline=True)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    return
    
def setup(bot):
  bot.add_cog(Cmds(bot))
