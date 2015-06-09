__author__ = 'zhangxg'

# import connector
from httplib import HTTPConnection, HTTPException
from urlparse import urlparse
import json

import api_config


url_root = 'http://' + api_config.config['endpoint_ip'] + ':' + str(api_config.config['endpoint_port'])

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
    body = {"auth": {"tenantName": tenant_name, "passwordCredentials": {"username": api_config.config['user_name'],
                                                                        "password": api_config.config['user_password']}}}
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


print(json.dumps(request_vms('admin')))


# fixme: how to define the class static
# fixme: make the variable global scope, singleton

# class Requester:
#
#     def request(self, method, url, body, header):
#
#         conn = connector.APIConnector()
#         connection = conn.get_connection()
#
#         try:
#             connection.request(method, url, json.dumps(body), header)
#             response = connection.getresponse()
#
#             if response.status > 299:
#                 return False
#
#             return response.read()
#         except HTTPException:
#             return False
#         finally:
#             connection.close()