import utils
import datetime


def handlerWriteParquetFile(arrData: list[dict], newDt: datetime, folderNameFormat: str, outputDir: str, tickerObj: dict, threadId: int):
    np_df = utils.arrayToDF(arrData, ['open'])
    folderName = newDt.strftime(folderNameFormat)
    path = '%s/%s' % (outputDir, folderName)
    utils.validateDirPath(path)
    utils.writeParquetFile(np_df, path, tickerObj['name'])
    print('Thread: ', threadId, ' ticker shots added to file')
