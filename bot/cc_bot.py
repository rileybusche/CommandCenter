import discord
import os
import subprocess
import json
import boto3
import time

import bot_controls
# import server_logging as log

client = discord.Client()

bot_owner = "LiquidLuck#9488"

authorized_users = [
    'LiquidLuck#9488',
    'PoshPrincess7#5589',
    'McNuggetMan#5562'
]

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

    if author == client.user or str(author) not in authorized_users:
        return
    
    # Outputs metrics of EC2 instance
    if msg == "!metrics":
        # metrics = os.popen('cat iostat').read()
        metrics = subprocess.check_output('iostat', shell=True).decode('utf-8')
        output = "Command Center Metrics\n" + metrics
        await channel.send(f'```fix\n{output}```')

    # Starts the Minecraft server and outputs IP address
    if msg == '!minecraft_start' and author == bot_owner:
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        for instance in instances:
            for tag in instance.tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'Minecraft Server':
                    if instance.state['Name'] == 'running':
                        await channel.send(f'```fix\nServer is already running | IP : {instance.public_ip_address}```')
                    elif instance.state['Name'] == 'stopped':
                        response = instance.start()
                        time.sleep(5)
                        await channel.send(f'```fix\nIP : {instance.public_ip_address}```')
    # Stops the Minecraft EC2 server
    if msg == '!minecraft_stop' and author == bot_owner:
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        for instance in instances:
            for tag in instance.tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'Minecraft Server':
                    if instance.state['Name'] == 'stopped':
                        await channel.send(f'```fix\nServer is already stopped.```')
                    elif instance.state['Name'] == 'running':
                        response = instance.stop()
                        # log.write_log(f'{response}', client)
                        await channel.send(f'```fix\nStopping Server```')

    # Lists out the exisiting instances
    if msg == '!instances' and author == bot_owner:
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        instances = ec2.instances.all()
        output = ''
        for instance in instances:
            if instance.state['Name'] != 'terminated':
                name = ''
                state = instance.state['Name']
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                output += f'{instance.instance_id} | {name} |  {instance.public_ip_address} | {state}\n'
        await channel.send(f'```fix\n{output}```')


    if msg.startswith('!update') and author == bot_owner:
        msg_tokens = msg.split(' ')
        output = bot_controls.update_bot(msg_tokens[1])
        print(output)
        await channel.send(f'```fix\nUpdating {msg_tokens[1]}```')

        # log.write_log(f'Updating {msg_tokens[1]}', client)
    
    if msg == '!update spotify' and  author == authorized_users

    if msg == '!bot_close_cc' and author == bot_owner:
        await client.close()

@client.event
async def on_ready():
    global connected_guilds
    # bot_controls.start_bots()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)