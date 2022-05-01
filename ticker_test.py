from thor_requests.connect import Connect
from datetime import datetime
import time

c = Connect("https://mainnet.veblocks.net")



for block in c.ticker():
    current_block = block
    print(datetime.utcfromtimestamp(current_block['timestamp']), current_block['number'])