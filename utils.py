import json
import numpy as np
import pandas as pd
from fastparquet import write
import os


def writeParquetFile(df, path, fileName):
    write(path + '/' + fileName + '.parq', df)


def readJsonFile(path):
    f = open(path)
    jsonContent = json.load(f)
    f.close()
    return jsonContent


def arrayToDF(arr):
    np_arr = np.array(arr)
    return pd.DataFrame(np_arr, columns=['open'])


def validateDirPath(path):
    if not os.path.exists(path):
        os.makedirs(path)
