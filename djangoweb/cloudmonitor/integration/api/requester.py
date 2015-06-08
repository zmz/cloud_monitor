__author__ = 'zhangxg'

import connector
from httplib import HTTPException
import json


url_root = 'http://' + connector.config['endpoint_ip'] + ':' + str(connector.config['endpoint_port'])

class Requester:

    def request(self, method, url, body, header):

        conn = connector.APIConnector()
        connection = conn.get_connection()

        try:
            connection.request(method, url, json.dumps(body), header)
            response = connection.getresponse()

            if response.status > 299:
                return False

            return response.read()
        except HTTPException:
            return False
        finally:
            connection.close()


def request_token(tenant_name):
    url = url_root + '/v2.0/tokens'
    body = {"auth": {"tenantName": tenant_name, "passwordCredentials": {"username": connector.config['user_name'], "password": connector.config['user_password']}}}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    request = Requester()
    return request.request('POST', url, body, headers)


print(request_token('admin'))