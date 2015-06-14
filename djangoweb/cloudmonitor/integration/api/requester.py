__author__ = 'zhangxg'

# import connector
from httplib import HTTPConnection, HTTPException
from urlparse import urlparse
import json

# import api_config

config = {
    'endpoint_ip': '10.120.16.100',
    'endpoint_port': 5000,
    # 'user_name': 'fopadmin',
    # 'user_password': 'YG86R-jkE',
    'user_name': 'admin',
    'user_password': 'admin123',
    'timeout': 30
}


url_root = 'http://' + config['endpoint_ip'] + ':' + str(config['endpoint_port'])

base_header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

token = {}
service_catalog = {}


def get_connection(url):
    parsed_url = urlparse(url)
    return HTTPConnection(parsed_url.hostname, parsed_url.port, {'timeout': 30})


def request(method, url, body, header):
        connection = get_connection(url)
        try:
            if body:
                body = json.dumps(body)
            connection.request(method, url, body, header)
            response = connection.getresponse()

            if response.status > 299:
                return False

            return json.loads(response.read()) # fixme: can return multiple values??

            # return response  #fixme: when connection closed, this value gone.
        except HTTPException, e:
            raise e
        finally:
            connection.close()


def request_token(tenant_name):
    print('request token...')
    global token, service_catalog
    url = url_root + '/v2.0/tokens'
    body = {"auth": {"tenantName": tenant_name, "passwordCredentials": {"username": config['user_name'],
                                                                        "password": config['user_password']}}}
    data = request('POST', url, body, base_header)
    if not data.get('access'):
        raise Exception('Error getting the token for tenant' + tenant_name)

    token = data['access']

    if token.get('serviceCatalog'):
        for service in token['serviceCatalog']:
            catalog = {
                # 'name': service['name'],
                'type': service['type'],
                'endpoints': service['endpoints']
            }
            service_catalog.__setitem__(service['name'], catalog)
    return token


def request_all_projects(tenant_name):
    url = url_root + '/v2.0/tenants'
    # fixme: dictionary appending.
    if not token:
        request_token(tenant_name)

    # url = service_catalog['keystone']['endpoints'][0]['adminURL']
    # url += '/tenants'

    base_header['X-Auth-Token'] = token['token']['id']

    response = request('GET', url, None, base_header)
    tenants = response['tenants']
    return tenants


def request_volumes(tenant_name):

    if not token:
        request_token(tenant_name)

    url = service_catalog['cinder']['endpoints'][0]['publicURL']
    url += '/volumes/detail?all_tenants=1'

    base_header['X-Auth-Token'] = token['token']['id']
    # base_header['X-Auth-Project-Id'] = tenant_name
    # base_header['User-Agent'] = 'python-novaclient'

    response = request('GET', url, None, base_header)
    return response


def request_vms(tenant_name):
    if not token:
        request_token(tenant_name)

    url = service_catalog['nova']['endpoints'][0]['publicURL']
    url += '/servers/detail?all_tenants=1'

    base_header['X-Auth-Token'] = token['token']['id']
    response = request('GET', url, None, base_header)
    return response


def show_tenants_and_vm_statistics(tenant_name):

    all_tenants = request_all_projects(tenant_name)
    all_vms = request_vms(tenant_name)

    tenants_names = {}
    for tenant in all_tenants:
        tenants_names[tenant['id']] = tenant['name']

    tenants_number = all_tenants.__len__()
    vm_numbers = all_vms['servers'].__len__()
    active_vms = []
    for vm in all_vms['servers']:
        if vm['status'] == 'ACTIVE':
            active_vms.append(vm)

    vm_by_environment = {
        'dev': set(),
        'tst': set(),
        'prd': set(),
        'oth': set()
    }

    no_tenants_associated = []
    for vm in active_vms:
        if not tenants_names.get(vm['tenant_id']):
            no_tenants_associated.append(vm['tenant_id'])
            continue

        name = tenants_names[vm['tenant_id']]
        if name.startswith('DEV_'):
            vm_by_environment['dev'].add(vm['tenant_id'])
        elif name.startswith('TST_'):
            vm_by_environment['tst'].add(vm['tenant_id'])
        elif name.startswith('PRD_'):
            vm_by_environment['prd'].add(vm['tenant_id'])
        else:
            vm_by_environment['oth'].add(vm['tenant_id'])

    print(" ---- Overall Statistics ----- ")
    print('Tenants Total Number: ' + str(tenants_number))
    print('VM Total Number: ' + str(vm_numbers) + ', ' + str(active_vms.__len__()) + '(Active)')

    print('\n ---- Statistics by Environment ----- ')
    for env_key in vm_by_environment.keys():
        print(env_key + ': ' + str(vm_by_environment[env_key].__len__()))

    print('\nBelow tenant has no association:')
    for tenant in no_tenants_associated:
        print(tenant)


show_tenants_and_vm_statistics('admin')

# print(json.dumps(request_all_projects('admin')))
#
# print(json.dumps(request_vms('admin')))
