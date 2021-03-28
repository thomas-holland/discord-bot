# main python function for the boto
import os
import discord

client = discord.Client()

@client.event
async def on_ready(): # start up call
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # there is a message in a channel that the bot has access to
    if message.author == client.user: # checks if the message was sent by the bot
        return # ignore the message (avoids loops)

    if message.content.startswith('hello'): # very basic hello script to test
        await message.channel.send('Hello!')


BOT_KEY = os.environ["BOT_KEY"] # gets the bot key from the host platform (so it is not hosted on github)
client.run(BOT_KEY) # run the bot with the bot key that was found