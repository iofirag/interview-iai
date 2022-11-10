import threading
import yfinance as yf
import time
from .fileHandler import handlerWriteParquetFile


def tickerHandler(data, shared_data):
    tickerShots = []
    while (not shared_data['latest_folder_path']):
        time.sleep(1)
    while (True):

        tickerRes = yf.Ticker(data['name'])
        # store data
        tickerShots.append({'open': tickerRes.info['open']})

        # append thread data to file
        threadId = threading.current_thread().ident
        handlerWriteParquetFile(
            tickerShots,
            shared_data["latest_folder_path"],
            data['name'], threadId)

        # clean thread data
        tickerShots = []
        time.sleep(data['freq'])
