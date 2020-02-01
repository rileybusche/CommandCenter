import discord
import os
import json

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)

token = creds['Credentials']['Command Center']['Token']

client = discord.Client()

@client.event
async def on_message(message):

    author = message.author
    channel = message.channel
    msg =  message.content.strip().lower()

    if author == client.user:
        return
    
    if msg == "!metrics":
        metrics = os.popen('cat iostat')
        await channel.send(f'```fix\n{metrics}```')

@client.event
async def on_ready():
    global connected_guilds
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)