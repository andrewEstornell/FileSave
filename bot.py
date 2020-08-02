import discord as dis
import time
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')


async def read_chat():
    await client.wait_until_ready()
    msgs = []
    channel = client.get_channel(316738255846506506)
    #await channel.send('hello')
    messages = await channel.history(limit=200).flatten()
    f = open('chat.txt', 'w')
    for m in messages:
        if len(m.content) > 0:
            f.write(str(m.content) +  '\n')
        if len(m.embeds) > 0:
            f.write(str(m.embeds) +  '\n')
        if len(m.attachments) > 0:
            for a in m.attachments:
                f.write(str(a.url) + '\n')







client.loop.create_task(read_chat())
read_chat()
client.run('NzM5NTIyNDU2OTEzNTc1OTc3.Xybr9Q.rCp8AJzTeEoZjpV1o84MXahsEL4')



