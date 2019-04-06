import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def test(self):
  async def on_member_join(self, member):
    await bot.say()

await bot.send_message(member, "Ahoj vítám tě na serveru GamingNetwork. přečti si prosím pravidla a faq") 
    
def setup(bot):
  bot.add_cog(Join(bot))
