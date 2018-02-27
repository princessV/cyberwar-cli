import argparse
import json
import os

CONFIG = None

def processing():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mode', choices=['init', 'launch'], required=True)
    parser.add_argument('-h', '--switch-host', default=CONFIG['network']['swicth']['host'])
    parser.add_argument('-p', '--switch-port', default=CONFIG['network']['swicth']['port'])
    parser.add_argument('-a', '--playground-address', default=CONFIG['network']['vnic']['playground_address'])
    args = parser.parse_args()
    run(args)

def run(args):
    if args.mode == 'init':
        command = 'PYTHONPATH={}/python/game/src/ python -m cyberwar.game --init={},{},{}'.format(CONFIG['cywe_path'], args.switch_host, args.switch_port, args.playground_address)
        os.system(command)
    elif args.mode == 'launch':
        command = 'PYTHONPATH={}/python/game/src/ python -m cyberwar.game --pypy={}'.format(CONFIG['cywe_path'], CONFIG['pypy_path'])
        os.system(command)
        pass

if __name__ == '__main__':
    global CONFIG
    with open('cwconfig.json', 'r') as f:
        CONFIG = json.load(f)
    processing()