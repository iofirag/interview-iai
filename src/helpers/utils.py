import os
import json
import numpy as np
import pandas as pd
from fastparquet import write


def writeParquetFile(df: pd.DataFrame.dtypes, path: str, fileName: str):
    full_file_path = path + '/' + fileName + '.parq'
    append = os.path.exists(full_file_path)
    write(full_file_path, df, append=append, mkdirs=True)


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
