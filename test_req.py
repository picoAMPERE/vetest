import requests
from datetime import datetime
import json
import time



def get_block(network, id_or_number: str = "best", expanded: bool = False) -> dict:
    """
        Get a block by id or number, default get "best" block
        If expanded is True, will return a block with expanded details.
    """
    url = f"https://{network}/blocks/{id_or_number}"
    if expanded:
        params = {'expanded': 'true'}
    else:
        params = {'expanded': 'false'}
    r = requests.get(
        url, params=params, headers={"accept": "application/json"})
    if not (r.status_code == 200):
        raise Exception(f"Cant connect to {url}, error {r.text}")
    return r.json()


while True:
    current_block = get_block("sync-mainnet.vechain.org")
    current_veblock = get_block("mainnet.veblocks.net")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Local: {current_time} |", 
          "sync-mainnet.vechain.org:", datetime.utcfromtimestamp(current_block['timestamp']), current_block['number'],
          "   mainnet.veblocks.net:", datetime.utcfromtimestamp(current_veblock['timestamp']), current_veblock['number'])
    time.sleep(1)