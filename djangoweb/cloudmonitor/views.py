
from django.template import RequestContext
from django.shortcuts import render

from django.http import HttpResponse

from . import dataprocessor

from ceilometer import extract

import time,json

import pdb


# Create your views here.


fileName = '/home/zhangxg/work/temp/openstack_prod_20150517_0518_2.data'


page_data = {};


def load_dash_board(request):
    return render(request, 'index.html')


def search(request):

    type = request.POST.get('type')
    time_start = time.strptime(request.POST.get('timestart'), '%m/%d/%Y %H:%M')
    time_end = time.strptime(request.POST.get('timeend'),'%m/%d/%Y %H:%M')

    result = extract.extract(time.strftime('%Y-%m-%d %H:%M', time_start), time.strftime('%Y-%m-%d %H:%M', time_end), type)

    request.session.__setitem__("search_result", result)

    # pdb.set_trace()

    # form_paras = {}

    imageIds = dataprocessor.getImageList(result)
    context = RequestContext(request, {'imageIdList': imageIds})
    return render(request, 'index.html', context)


def show_detail(request, resource_id, **paras):

    result = request.session.__getitem__('search_result')

    series = dataprocessor.getTimeSeriesDetail(result, resource_id, frequency=paras.get('frequency'))
#
    timestart = str(series.index[0])
    timeend = str(series.index[series.index.__len__() - 1])

    x_axis_string = "["
    for index in series.index:
        x_axis_string += '\'' + str(index) + "\',"
    x_axis_string = x_axis_string[0:x_axis_string.__len__()-1] + ']'

    y_axis = []
    for value in series.values:
        y_axis.append(value)

    context = RequestContext(request, {'legend_title': "[\'" + resource_id + "\']", 'x_axis': x_axis_string, 'y_axis': y_axis, 'imageIdList':result.keys, 'resource_id': resource_id, 'timestart': timestart, 'timeend': timeend})
    return render(request, 'index.html', context)
