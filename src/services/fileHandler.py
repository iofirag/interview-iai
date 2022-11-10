from helpers.utils import validateDirPath, arrayToDF, writeParquetFile
import time
from datetime import datetime


def handlerWriteParquetFile(arrData: list[dict], path: str, fileName: str, threadId: str):
    np_df = arrayToDF(arrData, ['open'])
    writeParquetFile(np_df, path, fileName)
    print('Thread: ', threadId, ' ticker shots added to file')


def folderFreqCreationHandler(data, shared_data):
    while True:
        folderName = datetime.now().strftime(data["folderNameFormat"])
        path = '%s/%s' % (data["outputDir"], folderName)
        validateDirPath(path)
        shared_data["latest_folder_path"] = path
        time.sleep(data["fileWriteFreqSeconds"])
