#! /bin/bash
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
sudo yum python3-pip -y
sudo python3 -m pip install -U discord.py
sudo python3 -m pip install apscheduler
sudo python3 -m pip install requests
# Import Creds
mkdir creds
# aws s3 cp s3://rb-int-us-east-1-bot-credentials/creds.json creds.json
# Ticker Bot
cd /home/ec2-user/
git clone https://github.com/rileybusche/TickerBotProd.git
cd TickerBotProd/TickerPriceBot/
touch api_key.txt
touch token.txt
# ShitPostBot
cd /home/ec2-user/
git clone https://github.com/rileybusche/ShitPostBot.git
cd ShitPostBot
touch token.txt
# Command Center Bot - Coming soon