import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot=commands.Bot(command_prefix='~')
bot.remove_command('help')

extensions = [ 'help', 'cmds']

async def my_background_task():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name='Developer')) 
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='Developer'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="~help"))
        await asyncio.sleep(10)
        
@bot.event
async def on_ready():
    print("hi")
    
if __name__ == '__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as error:
      print('{} cannot be loaded. [{}]'.format(extension, error))
 
bot.loop.create_task(my_background_task())
bot.run(os.environ['BOT_TOKEN'])
