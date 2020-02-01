import os

def start_bots():
    os.system('sh ./scripts/start_bots.sh')

def update_bot(name):
    cmd = f'sh ./scripts/update.sh {name}'
    os.system(cmd)