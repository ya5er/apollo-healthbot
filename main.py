import discord
import random

TOKEN = 'ODg4Nzg3MjE4NzAzOTk5MDE2.YUXxmQ.qR-61OtwZuJj2DWEqM3oKGU4Vxk'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)
