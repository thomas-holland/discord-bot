# main python function for the boto
import os
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='|')

@client.event
async def on_ready(): # start up call
    print('We have logged in as {0.user}'.format(client))

@bot.command()
async def test(ctx, *args):
    await ctx.send(args)


BOT_KEY = os.environ["BOT_KEY"] # gets the bot key from the host platform (so it is not hosted on github)
client.run(BOT_KEY) # run the bot with the bot key that was found