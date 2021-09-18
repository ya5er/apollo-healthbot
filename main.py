# import discord
# import random
#
# TOKEN = 'ODg4Nzg3MjE4NzAzOTk5MDE2.YUXxmQ.qR-61OtwZuJj2DWEqM3oKGU4Vxk'
#
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
# client.run(TOKEN)

import discord
import random

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 100 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if message.content == '!hello':
        response = "Hi, I am Apollo! Type !screen to proceed with the screening."
        await message.channel.send(response)
    elif message.content == '!screen':
        response = "Let the screening begin..."
        await message.channel.send(response)

    #if message.content.find("!hello") != -1:
        #await message.channel.send("Hi, I am Apollo! Type !screen to proceed with the screening.")
    


client.run("ODg4Nzg3MjE4NzAzOTk5MDE2.YUXxmQ.qR-61OtwZuJj2DWEqM3oKGU4Vxk")
# client.run(token)

print("I'm Online")