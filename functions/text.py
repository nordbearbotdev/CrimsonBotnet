import discord
import asyncio
import sys
import random
import os
import subprocess
import aiohttp
import socket
import time

client = discord.Client()

token = sys.argv[1] 
spam_text = sys.argv[2]

print(spam_text)
print(token)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await asyncio.sleep(0.8)
    await message.channel.send(spam_text)
    
client.run(token, bot=False)
