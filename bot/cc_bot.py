import discord
import os
import subprocess
import json

import bot_controls

client = discord.Client()

bot_owner = "LiquidLuck#9488"

log_channel_id = 673205358600388672

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)

token = creds['Credentials']['Command Center']['Token']


@client.event
async def on_message(message):

    author = message.author
    channel = message.channel
    msg =  message.content.strip().lower()

    if author == client.user or str(author) != bot_owner:
        return
    
    if msg == "!metrics":
        # metrics = os.popen('cat iostat').read()
        metrics = subprocess.check_output('iostat', shell=True).decode('utf-8')
        output = "Command Center Metrics\n" + metrics
        await channel.send(f'```fix\n{output}```')

    if msg.startswith('!update'):
        msg_tokens = msg.split(' ')
        bot_controls.update_bot(msg_tokens[1])

        log_channel = client.get_channel(log_channel_id)
        await log_channel.send(f'Updating {msg_tokens[1]}')
        

@client.event
async def on_ready():
    global connected_guilds
    bot_controls.start_bots()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)