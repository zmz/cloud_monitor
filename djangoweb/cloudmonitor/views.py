
from django.template import RequestContext
from django.shortcuts import render

from . import dataprocessor
from forms import ImageFilterForm

import time

import pdb


# Create your views here.


fileName = '/home/zhangxg/work/temp/yyyy.json'

def index(request):


    if request.method == 'POST':
        # post_info = []

        paras = {}
        error_message = []

        # paras['imageid'] = request.POST.get('imageid')

        if request.POST.get('timestart'):
            try:
                paras['timestart'] = time.strptime(request.POST.get('timestart'), '%Y-%m-%d')
            except TypeError:
                error_message.append("can not convert %s to a datetime" % request.POST.get('timestart'))
        if request.POST.get('timeend'):
            try:
                paras['timeend'] = time.strptime(request.POST.get('timeend'),'%Y-%m-%d')
            except TypeError:
                error_message.append("can not convert %s to a datetime" % request.POST.get('timeend'))

        if paras.get('timestart') and paras.get('timeend') and paras.get('timestart') > paras.get('timeend'):
            error_message.append('starttime' + request.POST.get('timestart') + ' is later than the end time ' + request.POST.get('timeend'))

        if request.POST.get('frequency'):
            try:
                paras['frequency'] = int(request.POST.get('frequency'))
            except ValueError:
                error_message.append('frequency should be integer')

        if error_message.__len__() > 0:
            data = dataprocessor.loadData(fileName)
            imageIds = dataprocessor.getImageList(data)
            context = RequestContext(request, {'imageIdList': imageIds,'postinfo': paras, 'error_message': error_message})
            return render(request, 'index.html', context)
        else:
            return getDiscInfoByPara(request, request.POST.get('imageid'), timestart=paras.get('timestart'), timeend=paras.get('timeend'), frequency=paras.get('frequency'))
    else:
        data = dataprocessor.loadData(fileName)
        imageIds = dataprocessor.getImageList(data)
        context = RequestContext(request, {'imageIdList': imageIds})
        return render(request, 'index.html', context)


def getDiscInfoByPara(request, disk_name, **paras):
    data = dataprocessor.loadData(fileName)
    series = dataprocessor.getTimeSeriesDetail(data, disk_name, frequency=paras.get('frequency'))

    timestart = str(series.index[0])
    timeend = str(series.index[series.index.__len__() - 1])

    x_axis_string = "["
    for index in series.index:
        x_axis_string += '\'' + str(index) + "\',"
    x_axis_string = x_axis_string[0:x_axis_string.__len__()-1] + ']'

    y_axis = []
    for value in series.values:
        y_axis.append(value)

    context = RequestContext(request, {'legend_title': "[\'" + disk_name + "\']", 'x_axis': x_axis_string, 'y_axis': y_axis, 'imageIdList':data.keys, 'imageid': disk_name, 'timestart': timestart, 'timeend': timeend})
    return render(request, 'index.html', context)