
from django.template import RequestContext
from django.shortcuts import render

from django.http import HttpResponse

from . import dataprocessor

from ceilometer import extract, extract_by_project_id

from ceilometer.user_authentication import Authentication

import time,json

from datetime import datetime, timedelta

import pdb


# Create your views here.
#
# fileName = '/home/zhangxg/work/temp/tenents_sample2.json'
#
# data = json.load(open(fileName, 'r'))

response_kwargs = {'content_type': 'application/json'}

page_data = {};


def get_tenents(request):

    # controller_ip = "192.168.232.129"
    controller_ip = "10.120.16.100"
    username = "admin"
    # password = "cloud1234"
    password = "admin123"
    project_name = None
    port = "35357"
    authObject = Authentication(controller_ip,username,password,project_name=None,port=port)
    authObject.set_service_clint_agent("keystoneclient")
    context = {'tenents': json.dumps(authObject.get_all_projects())}
    return HttpResponse(json.dumps(context), **response_kwargs)
    # return render(request, 'index4py.html', context)

def get_tenent_detail(request, tenent_name, time_off_set=-1):
    data_array = []

    now = datetime.now()
    delta = timedelta(days=time_off_set)

    if time_off_set > 0:
        time_begin = now
        time_end = now + delta
    else:
        time_begin = now + delta
        time_end = now

    data = extract_by_project_id.extract(time_begin.__format__('%Y-%m-%d %H:%M'), time_end.__format__('%Y-%m-%d %H:%M'), tenent_name)

    for key in data.keys():
        vm = {
            'vm_id': key,
            'detail': data.get(key)
        }
        data_array.append(vm)
    context = RequestContext(request, {'tenent_detail': json.dumps(data_array)})
    return render(request, 'index4py.html', context)


def load_dash_board(request):
    controller_ip = "10.120.16.100"
    username = "admin"
    password = "admin123"
    port = "35357"
    authObject = Authentication(controller_ip,username,password,project_name=None,port=port)
    authObject.set_service_clint_agent("keystoneclient")
    context = {'tenents': json.dumps(authObject.get_all_projects())}
    return render(request, 'tenents_list.html', context)


def search(request):

    form_paras = {}

    form_paras['type'] = request.POST.get('type')
    form_paras['timestart'] = request.POST.get('timestart')
    form_paras['timeend'] = request.POST.get('timeend')

    request.session.__setitem__('form_paras', form_paras)

    type = request.POST.get('type')
    time_start = time.strptime(request.POST.get('timestart'), '%m/%d/%Y %H:%M')
    time_end = time.strptime(request.POST.get('timeend'),'%m/%d/%Y %H:%M')

    result = extract.extract(time.strftime('%Y-%m-%d %H:%M', time_start), time.strftime('%Y-%m-%d %H:%M', time_end), type)

    request.session.__setitem__("search_result", result)
    resources = dataprocessor.get_resource_display_names(result)

    request.session.__setitem__('resource_id_list', resources)
    context = RequestContext(request, {'resource_list': resources, 'timestart': request.POST.get('timestart'), 'timeend': request.POST.get('timeend') })
    return render(request, 'index.html', context)


def show_detail(request, resource_id, **paras):

    result = request.session.__getitem__('search_result')
    resources = request.session.__getitem__('resource_id_list')
    form_paras = request.session.__getitem__('form_paras')

    first_element = result.get(resource_id).get('list')[0]

    counter_name = first_element.get('counter_name')
    counter_unit = first_element.get('counter_unit')


    series = dataprocessor.getTimeSeriesDetail(result, resource_id, frequency=paras.get('frequency'))

    x_axis_string = "["
    for index in series.index:
        x_axis_string += '\'' + str(index) + "\',"
    x_axis_string = x_axis_string[0:x_axis_string.__len__()-1] + ']'

    y_axis = []
    for value in series.values:
        y_axis.append(value)

    context = RequestContext(request,
                             {'graph_title': '\"' + counter_name + ' ( ' + counter_unit + ' )\"',
                              'legend_title': "[\'" + resource_id + "\']",
                              'x_axis': x_axis_string,
                              'y_axis': y_axis,
                              'resource_list': resources, 'resource_id': resource_id, 'timestart': form_paras['timestart'],
                              'timeend': form_paras['timeend']})
    return render(request, 'index.html', context)




