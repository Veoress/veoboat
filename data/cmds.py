import discord
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
  async def ping(self, ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await self.bot.send_typing(channel)
    t2 = time.perf_counter()
    await self.bot.say("**ping:** {} ms".format(round((t2-t1)*1000)))

    
def setup(bot):
  bot.add_cog(Cmds(bot))
