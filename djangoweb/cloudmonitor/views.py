
from django.template import RequestContext
from django.shortcuts import render

from . import dataprocessor


# Create your views here.


fileName = '/home/zhangxg/work/temp/yyyy.json'


def index(request):
    x_axis = ['2011Sep21','2011Oct5','2011Oct20','2011Nov5','2011Nov10','2011Nov14','2011Nov18','2011Nov21','2011Dec1','2011Dec2', '2011Dec3']
    x_string = '['
    for item in x_axis:
        x_string += '\'' + item + "\',"
    x_string = x_string[0:x_string.__len__()-1] + ']'

    y_axis = [1,6,5,6,3,1,7,10,11,2, 100]
    context = RequestContext(request, {'x_axis': x_string, 'y_axis': y_axis})
    return render(request, 'chartIndex.html', context)


def getDiscInfo(request):
    disk_name = "1ab42e12-47f8-40b8-9e56-6fcc6833f032"
    series = dataprocessor.process_json(fileName, disk_name)
    x_axis_string = "["
    for index in series.index:
        x_axis_string += '\'' + str(index) + "\',"
    x_axis_string = x_axis_string[0:x_axis_string.__len__()-1] + ']'

    y_axis = []
    for value in series.values:
        y_axis.append(value)

    context = RequestContext(request, {'legend_title': "[\'" + disk_name + "\']", 'x_axis': x_axis_string, 'y_axis': y_axis})
    return render(request, 'chartIndex.html', context)