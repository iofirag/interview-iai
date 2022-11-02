import os
import json
import numpy as np
import pandas as pd
from fastparquet import write


def writeParquetFile(df: pd.DataFrame.dtypes, path: str, fileName: str):
    write(path + '/' + fileName + '.parq', df)


def readJsonFile(path: str):
    f = open(path)
    jsonContent = json.load(f)
    f.close()
    return jsonContent


def arrayToDF(arr: list[dict], columns: list[str]):
    np_arr = np.array(arr)
    return pd.DataFrame(np_arr, columns=columns)


def validateDirPath(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
