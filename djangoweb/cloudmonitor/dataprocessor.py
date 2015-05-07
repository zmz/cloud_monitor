__author__ = 'zhangxg'

import json
import pandas as pd

def getTimeSeriesDetail(data, discName, **kwargs):
    time_serials = []
    values = []
    element = data[discName]
    for point in element['list']:
        try:
            time_serials.append(point['recorded_at'])
            values.append(point['counter_volume'])
        except TypeError:
            pass

    if kwargs.get('frequency'):
        return pd.Series(values, index=pd.to_datetime(time_serials)).sort_index().resample(str(kwargs.get('frequency')) + 'Min', how='mean')
    else:
        return pd.Series(values, index=pd.to_datetime(time_serials)).sort_index()


def getImageSummary(data, discName):
    #todo
    pass


def getImageList(data):
    return data.keys


def loadData(pathToFile):
    return json.load(open(pathToFile, 'r', 100))


    # for index in pandas_serial.index:
    #     print(index)
    #
    # print(pandas_serial.index)
    # print(pandas_serial.values)


fileName = '/home/zhangxg/work/temp/yyyy.json'
print(getTimeSeriesDetail(loadData(fileName), "1ab42e12-47f8-40b8-9e56-6fcc6833f032"))







