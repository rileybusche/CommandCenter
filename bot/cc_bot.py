import discord
import os
import subprocess
import json
import boto3

import bot_controls
import server_logging as log

client = discord.Client()

bot_owner = "LiquidLuck#9488"

with open('/home/ec2-user/creds/creds.json') as file:
    creds = json.load(file)
# with open('creds.json') as file:
#     creds = json.load(file)

token = creds['Credentials']['Command Center']['Token']


@client.event
async def on_message(message):

    author = message.author
    channel = message.channel
    msg =  message.content.strip().lower()

    if author == client.user or str(author) != bot_owner:
        return
    
    # Outputs metrics of EC2 instance
    if msg == "!metrics":
        # metrics = os.popen('cat iostat').read()
        metrics = subprocess.check_output('iostat', shell=True).decode('utf-8')
        output = "Command Center Metrics\n" + metrics
        await channel.send(f'```fix\n{output}```')

    # Starts the Minecraft server and outputs IP address
    if msg == '!minecraft_start':
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        for instance in instances:
            for tag in instance.tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'Minecraft Server':
                    if instance.state['Name'] == 'running':
                        await channel.send(f'```fix\nServer is already running.```')
                    elif instance.state['Name'] == 'stopped':
                        response = instance.start()
                        await channel.send(f'```fix\n{response}```')
    # Stops the Minecraft EC2 server
    if msg == '!minecraft_stop':
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        for instance in instances:
            for tag in instance.tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'Minecraft Server':
                    if instance.state['Name'] == 'stopped':
                        await channel.send(f'```fix\nServer is already stopped.```')
                    elif instance.state['Name'] == 'running':
                        response = instance.stop()
                        await channel.send(f'```fix\n{response}```')

    # Lists out the exisiting instances
    if msg == '!instances':
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        output = ''
        for instance in instances:
            if insance.state['Name'] != 'terminated':
                name = ''
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                output += f'{name} | {instance.instance_id} | {instance.public_ip_address} | {instance.state['Name']}\n'
        await channel.send(f'```fix\n{output}```')


    if msg.startswith('!update'):
        msg_tokens = msg.split(' ')
        bot_controls.update_bot(msg_tokens[1])

        log.write_log(f'Updating {msg_tokens[1]}', client)

@client.event
async def on_ready():
    global connected_guilds
    # bot_controls.start_bots()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)