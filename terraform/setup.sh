#! /bin/bash
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
sudo yum python3-pip -y
sudo python3 -m pip install -U discord.py
sudo python3 -m pip install apscheduler
sudo python3 -m pip install requests
sudo python3 -m pip install matplotlib
sudo python3 -m pip install textblob
sudo python3 -m textblob.download_corpora
sudo python3 -m pip install boto3

# Import From S3
cd /home/ec2-user/
mkdir creds
cd /home/ec2-user/creds
sudo aws s3 cp s3://rb-int-us-east-1-bot-credentials/creds.json creds.json

# Ticker Bot
cd /home/ec2-user/
git clone https://github.com/rileybusche/TickerBotProd.git

# ShitPostBot
cd /home/ec2-user/
git clone https://github.com/rileybusche/ShitPostBot.git

# Dom Bot
cd /home/ec2-user/
git clone https://github.com/rileybusche/DomBot.git

# Command Center Bot
cd /home/ec2-user/
git clone https://github.com/rileybusche/CommandCenter.git
cd /home/ec2-user/

# Start Bots
sudo nohup python3 /home/ec2-user/TickerBotProd/TickerPriceBot/tpb_bot.py &
sudo nohup python3 /home/ec2-user/ShitPostBot/spb_bot.py &
sudo nohup python3 /home/ec2-user/CommandCenter/bot/cc_bot.py &



