import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_member_join(self, member):
    await self.bot.send_message(member, "Ahoj vítám tě na serveru PandaGaming. přečti si prosím #⌦📚rules ") 
    
def setup(bot):
  bot.add_cog(Join(bot))
