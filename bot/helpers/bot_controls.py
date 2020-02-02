import os

def start_bots():
    os.system('sh ./scripts/start_bots.sh')
    bots = ['tpb', 'spb']
    print("Starting Bots...")
    for bot in bots:
        update_bot(bot)

def update_bot(name):
    cmd = f'sh ./scripts/update.sh {name}'
    os.system(cmd)