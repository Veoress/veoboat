import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime
import time
from flask import Flask
from threading import Thread
import youtube_dl

app = Flask('')
client = discord.Client()

def run():
  app.run(host='0.0.0.0',port=8080)

@app.route('/',methods=["HEAD","GET"])
def home():
  keep_alive()
  return "cool"

bot = commands.Bot(command_prefix='~', status=discord.Status.idle, activity=discord.Game(name="Booting.."))

@bot.event
async def on_ready():
    print ("Connected to Discord")
    listen_list = ["~help", "~ | prefix", "Developed by ×Vēørēs×#0095", "GamingNetwork Server"]
    while True:
        await bot.change_presence(game=discord.Game(name=random.choice(listen_list), type=2))
        await asyncio.sleep(6)

bot.remove_command("help")

players = {}

@bot.event
async def on_message(message):
        await bot.process_commands(message)

@bot.command()
async def fortmap():
	await bot.say('https://media.deseretdigital.com/file/8d92395855?resize=width_1200&type=jpg&c=6&a=e0717f4c')
@bot.command()
async def rdance():
	await bot.say('https://media.discordapp.net/attachments/518083878817234944/531040356217651200/ds_rainbow_dance.gif?width=84&height=84')
@bot.command()
async def help():
	await bot.say('**4 |General:** `ping, ahoj, help, userinfo`')
	await bot.say('**3 |Fun:** `number, rdance, fortmap`')
	await bot.say('**2 |Bot:** `invite, veo_server`')
@bot.command()
async def invite():
	await bot.say('Invite: https://discordapp.com/oauth2/authorize?client_id=563996504680038410&permissions=2146958839&scope=bot')
@bot.command()
async def gn_server():
	await bot.say('Veoresův Server: https://discord.gg/EFzU2qu')
@bot.command()
async def ahoj():
	await bot.say('__**Ahoj :D**__')
@bot.command()
async def ping():
	await bot.say('Pong!')
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member=None):
    if not user:
      user = ctx.message.author

    embed=discord.Embed(title="test", description="test", color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    await self.bot.send_message(ctx.message.channel, embed=embed)
@bot.command(pass_context=True)
async def number(ctx):
	await bot.say(random.randint(1,100))
