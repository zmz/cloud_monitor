__author__ = 'zhangxg'

'''---the api configuration ----------- '''
api_configs = {
    'endpoint_ip': '10.120.16.100',
    'endpoint_port': 5000,
    'user_name': 'admin',
    'user_password': 'admin123',
    'timeout': 30
}

'''--- mongo configuration ----------- '''
mongo_configs = {
    'mongo_host': '10.120.16.101',
    'mongo_port': 27017,
    'mongo_database': 'ceilometer',
    'mongo_db_user': 'ceilometer',
    'mongo_db_password': 'ou25svNk'
}


def get_api_config():
    return api_configs


def get_mongo_config():
    return mongo_configs