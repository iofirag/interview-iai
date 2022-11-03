import threading
import sys
sys.path.insert(1, 'helpers')
sys.path.insert(1, 'services')
from fetchTicker import tickerHandler
from fileHandler import folderFreqCreationHandler
from utils import readJsonFile


if __name__ == "__main__":
    config = readJsonFile('./config/config.json')
    tickerList = readJsonFile('./config/tickers.json')
    shared_data = {
        "latest_folder_path": ''
    }

    folderFreqCreationThreadData = {
        "fileWriteFreqSeconds": config["fileWriteFreqSeconds"],
        "outputDir": config["outputDir"],
        "folderNameFormat": config["folderNameFormat"],
    }
    folderFreqCreationThread = threading.Thread(target=folderFreqCreationHandler, args=(
        folderFreqCreationThreadData, shared_data))
    folderFreqCreationThread.start()

    for tickerObj in tickerList:
        tickerThreadData = {
            "name": tickerObj["name"],
            "freq": tickerObj["freq"],
            "outputDir": config["outputDir"],
            "folderNameFormat": config["folderNameFormat"],
            "fileWriteFreqSeconds": config["fileWriteFreqSeconds"],
        }
        ti = threading.Thread(target=tickerHandler, args=(
            tickerThreadData, shared_data))
        ti.start()
