__author__ = 'zhangxg'

import json
import pandas as pd

def process_json(pathToFile, discName):
    data = json.load(open(pathToFile, 'r', 100))
    keys = data.keys()
    time_serials = []
    values = []

    element = data[discName]
    for point in element['list']:
        try:
            time_serials.append(point['recorded_at'])
            values.append(point['counter_volume'])
        except TypeError:
            pass

    return pd.Series(values, index=pd.to_datetime(time_serials)).sort_index()

    # for index in pandas_serial.index:
    #     print(index)
    #
    # print(pandas_serial.index)
    # print(pandas_serial.values)


fileName = '/home/zhangxg/work/temp/yyyy.json'
print(process_json(fileName, "1ab42e12-47f8-40b8-9e56-6fcc6833f032"))







