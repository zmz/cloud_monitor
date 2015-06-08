__author__ = 'zhangxg'


import api.connector as connector


conn = connector.APIConnector()

print(conn.get_connection())