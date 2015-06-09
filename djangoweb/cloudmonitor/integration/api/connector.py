__author__ = 'zhangxg'

'''
this module connects the openstack api
'''

from httplib import HTTPConnection
from urlparse import urlparse


# from .. import config  fixme: the import not working

api_config = {
    'endpoint_ip': '10.120.16.100',
    'endpoint_port': 5000,
    'user_name': 'admin',
    'user_password': 'admin123',
    'timeout': 30
}


def get_connection(url):
    parsed_url = urlparse(url)
    return HTTPConnection(parsed_url.hostname, parsed_url.port, {'timeout': config['timeout']})

# class APIConnector:
#
#     def __init__(self):
#         # self.configs = config.get_api_config()
#         kwargs = {'timeout': config['timeout']}
#         self.connection = HTTPConnection(config['endpoint_ip'], config['endpoint_port'], kwargs)
#
#     def get_connection(self, url=None):
#
#         if url:
#             parsed_url = urlparse(url)
#             return HTTPConnection(parsed_url.hostname, parsed_url.port, {'timeout': config['timeout']})
#         else:
#             return self.connection
