import threading
from helpers.utils import readJsonFile
from services.fileHandler import folderFreqCreationHandler
from services.fetchTicker import tickerHandler

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
    folderFreqCreationThread = threading.Thread(
        target=folderFreqCreationHandler, args=(
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
