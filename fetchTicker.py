import threading
import yfinance as yf
import time
import fileHandler
from datetime import datetime


def tickerHandler(tickerObj: dict, config: dict):
    tickerShots = []
    lastFileWrite = datetime.now()
    while (True):
        tickerRes = yf.Ticker(tickerObj['name'])
        newDt = datetime.now().replace(second=0, microsecond=0)
        # store data
        tickerShots.append({'open': tickerRes.info['open']})

        # check wether passed time divide to seconds bigger than zero
        diff = int(round(newDt.timestamp() - lastFileWrite.timestamp()))
        if (diff // config["fileWriteFreqSeconds"] > 0):
            threadId = threading.current_thread().ident

            # save thread data to file
            fileHandler.handlerWriteParquetFile(
                tickerShots, newDt, config["folderNameFormat"],
                config["outputDir"], tickerObj, threadId)

            # clean thread data
            tickerShots = []
            lastFileWrite = newDt
        time.sleep(tickerObj['freq'])
