import discord, os, time
from discord.ext import tasks, commands
import asyncio

# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
# token = os.getenv("TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
token = "ODQzODI5ODI4MzczMTg0NTIy.YKcNTg.AIrq37xjKY4jYkzqyucgRraeTmk"

bot = commands.Bot(command_prefix = "-", self_bot=True)
#sleep = 10

@bot.event
async def on_ready():
    print("InfinityTrades Human Bot Online!")
    channel = bot.get_channel(842343909165760522)
    await channel.send("bot enabled")
    await bot.change_presence(status=discord.Status.online)
    bot.loop.create_task(status_task())
    #bot.loop.create_task(bump_task())

@bot.event
async def on_message(message: discord.Message):
  
    #fusion alerts
    if message.author.id == 836095711061082142 and message.channel.id == 832455360035553320:  
        channel = bot.get_channel(842343909165760522)
        embeds = message.embeds # return list of embeds
        for embed in embeds:
            toembed = embed.to_dict()
            await channel.send(toembed)         
            await channel.send(toembed['description'])
            await channel.send(toembed['title'])
            await channel.send(toembed['footer'])       
            await channel.send(toembed['author'])
            for field in toembed['fields']:
                await channel.send(field)
                await channel.send(field['name'])     
                await channel.send(field['value'])

    #ghazi alerts
    if message.author.id == 835340100769939466 and message.channel.id == 829852867292692501:  
        channel = bot.get_channel(842343909165760522)
        embeds = message.embeds # return list of embeds
        for embed in embeds:
            toembed = embed.to_dict()
            await channel.send(toembed)         
            await channel.send(toembed['description'])
            await channel.send(toembed['title'])
            await channel.send(toembed['footer'])       
            await channel.send(toembed['author'])
            for field in toembed['fields']:
                await channel.send(field)
                await channel.send(field['name'])     
                await channel.send(field['value'])

    #byrce alerts
    if message.author.id == 387234780523134980 and message.channel.id == 800376137884106752:  
        channel = bot.get_channel(842343909165760522)
        #await channel.send(message.content.replace("Bryce", ""))
        if "BTO" in message.content.split()[0]:
            embed = discord.Embed(title=f'{message.content.split()[0]} {message.content.split()[1]} {message.content.split()[2]} {message.content.split()[3]} {message.content.split()[4]}', 
            description=f'{message.content.split()[0]}\nTicker: {message.content.split()[1]}\nStrike: {message.content.split()[2]}\nExpiration: {message.content.split()[3]}\nPrice: {message.content.split()[4]}', colour=discord.Colour.green())
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/825152063775965215/3819a7dc11f547fadb770c5fc167c37d.png')
            await channel.send(embed=embed)
        elif "STC" in message.content.split()[0]:
            embed = discord.Embed(title=f'{message.content.split()[0]} {message.content.split()[1]} {message.content.split()[2]} {message.content.split()[3]} {message.content.split()[4]}',
            description=f'{message.content.split()[0]}\nTicker: {message.content.split()[1]}\nStrike: {message.content.split()[2]}\nExpiration: {message.content.split()[3]}\nPrice: {message.content.split()[4]}', colour=discord.Colour.red())
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/825152063775965215/3819a7dc11f547fadb770c5fc167c37d.png')
            await channel.send(embed=embed)
   
  
    await bot.process_commands(message)

@bot.event
async def status_task():
   while True:
        await bot.change_presence(status=discord.Status.online)
        print('keeping alive')
        await asyncio.sleep(30)
"""
@bot.event
async def bump_task():
   while True:
        channel = bot.get_channel(800376137884106752)
        await channel.send("!d bump")
        print('bumping') 
        print(sleep)
        await asyncio.sleep(sleep)  
"""
bot.run(token)