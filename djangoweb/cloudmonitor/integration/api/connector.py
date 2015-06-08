__author__ = 'zhangxg'

'''
this module connects the openstack api
'''

from httplib import HTTPConnection, HTTPException


# from .. import config  fixme: the import not working

config = {
    'endpoint_ip': '10.120.16.100',
    'endpoint_port': 5000,
    'user_name': 'admin',
    'user_password': 'admin123',
    'timeout': 30
}


class APIConnector:

    def __init__(self):
        # self.configs = config.get_api_config()
        kwargs = {'timeout': config['timeout']}
        self.connection = HTTPConnection(config['endpoint_ip'], config['endpoint_port'], kwargs)

    def get_connection(self):
        return self.connection

    # def get_configuration(self):
    #     return self.configs