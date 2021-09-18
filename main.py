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

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        # If the user says !hello we will send back hi
        await message.channel.send("Hi, I am Apollo!")


client.run("ODg4Nzg3MjE4NzAzOTk5MDE2.YUXxmQ.qR-61OtwZuJj2DWEqM3oKGU4Vxk")
# client.run(token)

print("I'm Online")