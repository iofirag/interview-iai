import threading
import sys
sys.path.insert(1, 'helpers')
sys.path.insert(1, 'services')

from utils import readJsonFile
from fetchTicker import tickerHandler

if __name__ == "__main__":
    config = readJsonFile('./config/config.json')
    tickerList = readJsonFile('./config/tickers.json')

    for tickerObj in tickerList:
        t = threading.Thread(target=tickerHandler, args=(
            tickerObj, config))
        t.start()
