import threading
from utils import readJsonFile
from fetchTicker import tickerHandler


if __name__ == "__main__":
    config = readJsonFile('./config.json')
    tickerList = readJsonFile('./tickers.json')

    for tickerObj in tickerList:
        t = threading.Thread(target=tickerHandler, args=(
            tickerObj, config))
        t.start()
