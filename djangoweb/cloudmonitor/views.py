
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

    # return render(request, 'index.html')

    # if do_validation(request):
    #     return render(request, 'index.html')
    # else:
    #     context = RequestContext(request, {'page_data': page_data})
    #     return render(request, 'index.html', context)

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

    # imageIds = dataprocessor.getImageList(result)
    # context = RequestContext(request, {'imageIdList': imageIds, 'resource_id': resource_id})
    # return render(request, 'index.html', context)


# def do_validation(request):
#     form_paras = {}
#     error_message = []
#     if request.POST.get('timestart'):
#         try:
#             form_paras['timestart'] = time.strptime(request.POST.get('timestart'), '%Y-%m-%d')
#         except TypeError:
#             error_message.append("can not convert %s to a datetime" % request.POST.get('timestart'))
#     if request.POST.get('timeend'):
#         try:
#             form_paras['timeend'] = time.strptime(request.POST.gdet('timeend'),'%Y-%m-%d')
#         except TypeError:
#             error_message.append("can not convert %s to a datetime" % request.POST.get('timeend'))
#
#     if form_paras.get('timestart') and form_paras.get('timeend') and form_paras.get('timestart') > form_paras.get('timeend'):
#         error_message.append('starttime' + request.POST.get('timestart') + ' is later than the end time ' + request.POST.get('timeend'))
#
#     if request.POST.get('frequency'):
#         try:
#             form_paras['frequency'] = int(request.POST.get('frequency'))
#         except ValueError:
#             error_message.append('frequency should be integer')
#
#     page_data['form_paras'] = form_paras;
#     if error_message.__len__() > 0:
#         page_data['form_errors'] = error_message
#         return False
#     else:
#         page_data['form_errors'] = {}
#         return True




# def tryAjax(request):
#     return render(request, 'tryajax.html')
#
#
# def getdata(request):
#
#     # pdb.set_trace()
#     context = {'name': 'zhang'}
#     response_kwargs = {}
#     response_kwargs['content_type'] = 'application/json'
#     return HttpResponse(json.dumps(context), **response_kwargs)


# def index(request):
#     if request.method == 'POST':
#         paras = {}
#         error_message = []
#
#         if request.POST.get('timestart'):
#             try:
#                 paras['timestart'] = time.strptime(request.POST.get('timestart'), '%Y-%m-%d')
#             except TypeError:
#                 error_message.append("can not convert %s to a datetime" % request.POST.get('timestart'))
#         if request.POST.get('timeend'):
#             try:
#                 paras['timeend'] = time.strptime(request.POST.get('timeend'),'%Y-%m-%d')
#             except TypeError:
#                 error_message.append("can not convert %s to a datetime" % request.POST.get('timeend'))
#
#         if paras.get('timestart') and paras.get('timeend') and paras.get('timestart') > paras.get('timeend'):
#             error_message.append('starttime' + request.POST.get('timestart') + ' is later than the end time ' + request.POST.get('timeend'))
#
#         if request.POST.get('frequency'):
#             try:
#                 paras['frequency'] = int(request.POST.get('frequency'))
#             except ValueError:
#                 error_message.append('frequency should be integer')
#
#         if error_message.__len__() > 0:
#             data = dataprocessor.loadData(fileName)
#             imageIds = dataprocessor.getImageList(data)
#             context = RequestContext(request, {'imageIdList': imageIds,'postinfo': paras, 'error_message': error_message})
#             return render(request, 'index.html', context)
#         else:
#             return getDiscInfoByPara(request, request.POST.get('imageid'), timestart=paras.get('timestart'), timeend=paras.get('timeend'), frequency=paras.get('frequency'))
#     else:
#         data = dataprocessor.loadData(fileName)
#         imageIds = dataprocessor.getImageList(data)
#         context = RequestContext(request, {'imageIdList': imageIds})
#         return render(request, 'index.html', context)


# def getDiscInfoByPara(request, disk_name, **paras):
#     data = dataprocessor.loadData(fileName)
#     series = dataprocessor.getTimeSeriesDetail(data, disk_name, frequency=paras.get('frequency'))
#
#     timestart = str(series.index[0])
#     timeend = str(series.index[series.index.__len__() - 1])
#
#     x_axis_string = "["
#     for index in series.index:
#         x_axis_string += '\'' + str(index) + "\',"
#     x_axis_string = x_axis_string[0:x_axis_string.__len__()-1] + ']'
#
#     y_axis = []
#     for value in series.values:
#         y_axis.append(value)
#
#     context = RequestContext(request, {'legend_title': "[\'" + disk_name + "\']", 'x_axis': x_axis_string, 'y_axis': y_axis, 'imageIdList':data.keys, 'imageid': disk_name, 'timestart': timestart, 'timeend': timeend})
#     return render(request, 'index.html', context)