__author__ = 'zhangxg'

import json
import pandas as pd

from ceilometer import extract, cfg

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


# result = extract.extract(cfg.TIME_BEGIN, cfg.TIME_END, "cpu")

# print(result.keys())





