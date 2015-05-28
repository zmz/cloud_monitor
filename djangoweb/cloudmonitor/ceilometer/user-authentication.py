

from utils import json_request

try:
    import json
except ImportError:
    import simplejson as json

class Authentication():

    def __init__(self,controller_ip,username,password,project_name=None,port=None):
        if None == project_name:
            self.project_name = "admin"
        else:
            self.project_name = project_name
        self.username = username
        self.password = password
        if None == port:
            self.port = "5000"
        else:
            self.port = port
        self.endpoint_url = "http://%s:%s" %(controller_ip,self.port)
        self.user_agent = "keystoneclient"

    def set_service_clint_agent(self,service_client_agent):
        if None != service_client_agent:
            self.user_agent = service_client_agent

    """
        uri:/v2.0/tokens
    """
    def get_user_access(self,uri="/v2.0/tokens"):

        url = self.endpoint_url+uri
        req_body = {"auth": {"tenantName": self.project_name, "passwordCredentials": {"username": self.username, "password": self.password}}}
        req_headers = {'Content-Type': 'application/json','User-Agent': 'python-%s'%(self.user_agent,)}
        result = json_request(url,'POST',req_body , req_headers)
        if not result.has_key("access"):
            raise Exception("get token error")
        return result["access"]


    """
        uri:/v2.0/tenants
        curl -i http://controller:35357/v2.0/tenants  -H "User-Agent: python-keystoneclient" -H "X-Auth-Token:509207ffc1aad85bc689"
    """
    def get_all_projects(self,uri="/tenants",token=None):
        user_access_str = self.get_user_access()
        keystone_endpoint_admin_url = self.get_service_accss_url_by_name(user_access_str,"keystone")
        url = keystone_endpoint_admin_url + uri
        req_body = {}
        req_headers =  {'User-Agent': 'python-%s'%(self.user_agent,)}
        if None == token:
            req_token = user_access_str["token"]["id"]
        else:
            req_token = token
        req_headers["X-Auth-Token"] = req_token
        result = json_request(url,'GET',req_body , req_headers)
        print result
        if type(result) == type(True):
            if result == False:
                raise Exception("response error .")
        if not result.has_key("tenants"):
            raise Exception("get project error")
        return result["tenants"]

    def get_service_accss_url_by_name(self,user_access_str,service_name):
        keystone_service_catalog = user_access_str["serviceCatalog"]
        keystone_endpoint_admin_url = None
        for service in keystone_service_catalog:
            if service["name"].strip() == service_name.strip():
                service_endpoints = service["endpoints"]
                for endpoint in service_endpoints:
                    if endpoint.has_key("adminURL"):
                        keystone_endpoint_admin_url = endpoint["adminURL"]
        return keystone_endpoint_admin_url


    def get_users_by_project_id(self,project_id):
        pass

    """
    curl -i 'http://controller:8774/v2/f59ae452a69544be9ccc886f0fe5e4d4/servers?all_tenants=True' -X GET
    -H "X-Auth-Project-Id: admin" -H "User-Agent: python-novaclient" -H "Accept: application/json" -H "X-Auth-Token:"
    """
    def get_all_vms(self,project_id,is_all_tenants=False):
        pass


if __name__ == "__main__":
    # controller_ip = "192.168.232.129"
    controller_ip = "10.120.16.100"
    username = "admin"
    # password = "cloud1234"
    password = "admin123"
    project_name = None
    port = "35357"
    authObject = Authentication(controller_ip,username,password,project_name=None,port=port)
    authObject.set_service_clint_agent("keystoneclient")
    print authObject.get_all_projects()