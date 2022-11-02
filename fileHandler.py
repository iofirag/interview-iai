import utils


def handlerWriteParquetFile(arrData, newDt, folderNameFormat, outputDir, tickerObj, threadId):
    np_df = utils.arrayToDF(arrData)
    folderName = newDt.strftime(folderNameFormat)
    path = '%s/%s' % (outputDir, folderName)
    utils.validateDirPath(path)
    utils.writeParquetFile(np_df, path, tickerObj['name'])
    print('Thread: ', threadId, ' ticker shots added to file')
