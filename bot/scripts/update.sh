#!/bin/bash
if [ $1 == "spb" ]
then
    echo "Updating SPB"
    cd /home/ec2-user/ShitPostBot/
    sudo git pull
    PIDS=$(echo | pgrep -f "spb_bot.py")
    sudo kill -9 $PIDS
    sudo nohup python3 spb_bot.py &
elif [ $1 == "tpb" ]
then
    echo "Updating TPB"
    cd /home/ec2-user/TickerBotProd/TickerPriceBot/
    sudo git pull
    PIDS=$(echo | pgrep -f "tpb_bot.py")
    sudo kill -9 $PIDS
    sudo nohup python3 tpb_bot.py &
elif [ $1 == "cc" ]
then
    echo "Updating CC"
    cd /home/ec2-user/CommandCenter/bot/
    sudo git pull
    PIDS=$(echo | pgrep -f "cc_bot.py")
    sudo kill -9 $PIDS
    sudo nohup python3 cc_bot.py &    
elif [ $1 == "db" ]
then
    echo "Updating DB"
    cd /home/ec2-user/DomBot/
    sudo git pull
    PIDS=$(echo | pgrep -f "dombot_bot.py")
    sudo kill -9 $PIDS
    sudo nohup python3 dombot_bot.py &
elif [ $1 == "spotify" ]
then
    echo "Updating Spotify"
    cd /home/ec2-user/spotify-discord-bot/
    sudo git pull
    PIDS=$(echo | pgrep -f "SpotifyBot.ts")
    sudo kill -9 $PIDS
    npm start SpotifyBot.ts &    
fi