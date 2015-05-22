__author__ = 'zhangxg'

import json
import pandas as pd

from ceilometer import extract, cfg

import pdb

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


def get_resource_display_names(data):
    resource_id_names = []
    for key in data.keys():
        resource = {}
        resource['resource_id'] = key
        display_name = data.get(key).get('display_name')
        if display_name:
            resource['display_name'] = display_name
        else:
            resource['display_name'] = key
        resource_id_names.append(resource)
    return resource_id_names


def getImageSummary(data, discName):
    #todoc

    pass


def getImageList(data):
    return data.keys


def loadData(pathToFile):
    return json.load(open(pathToFile, 'r', 100))



# result = extract.extract(cfg.TIME_BEGIN, cfg.TIME_END, "cpu")
#
# abc = get_resource_display_names(result)
#
# print(abc)

# print(result.keys())





