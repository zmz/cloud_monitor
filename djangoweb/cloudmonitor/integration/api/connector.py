from __future__ import with_statement

__author__ = 'zhangxg'

# from __future__ import with_statement

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

# class MyException(Exception):
#
#     def __init__(self):
#         self.code = 1
#         self.message = 'this is my exception'
#         self.__str__ = 'my exception returns a string'
#
#         # print('user defined')
#
#
# b = 10
# try:
#     try:
#         a = b / 0
#     except ZeroDivisionError as zero_exp:
#         #
#         print(zero_exp)
#     else:
#         print('this is internal else')
#
#     finally:
#         print('internal finally')
#
#     print zero_exp.message
#
# except MyException as myexp:
#     print('catch my exception' + myexp.message + str(myexp.code))
#
# else:
#     print('this is outer else')
#
# finally:
#     print('finally')
#
# # print(myexp)
# print('end of programming')


#
# with open('path.to.file', 'r') as file:
#     print(file.read())


class TraceBlock:
    def message(self, arg):
        print('running ' + arg)

    def __enter__(self):
        print('entering...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is None:
            print('exist normally...')
        else:
            print('raise excepiton... ' + str(exc_type))
            return False

if __name__ == '__main__':
    # with TraceBlock() as action:
    #     action.message('test 1')
    #     print('reached')
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')





