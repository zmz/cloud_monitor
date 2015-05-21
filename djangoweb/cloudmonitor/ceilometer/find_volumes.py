'''
@author: tianyuan8
'''


from utils import json_request

#endpoint = 'http://192.168.0.2:5000'

def _conn_keystone(ip,username="admin",password = "admin123" , port = "5000"):
    '''
    curl -i 'http://192.168.0.2:5000/v2.0/tokens' -X POST -H "Accept: application/json" -H "Content-Type: application/json" -H "User-Agent: python-novaclient" -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "admin123"}}}'
    
    return token id
    '''
    url =  "http://"+ip+":"+port+"/v2.0/tokens"
    data = {"auth": {"tenantName": "admin", "passwordCredentials": {"username": username, "password": password}}}
    headers = {'Content-Type': 'application/json','User-Agent': 'python-novaclient','Accept': 'application/json' }
    result = json_request(url,'POST',data , headers)
    if not result.has_key("access"):
        raise Exception("get token error")
    return result["access"]




def _query_volumes(result):
    '''
     curl -i 'http://10.120.16.100:8776/v1/42b779463dd4444eb5e575ea90e8a6b9/volumes/detail?all_tenants=1' -X GET -H "Accept: application/json" -H "User-Agent: python-novaclient" -H "X-Auth-Project-Id: admin" -H "X-Auth-Token: {SHA1}541ae6f7e88b9272974ce4a93cad39f21eb767a8"
    '''

    data = {}
    url = ""
    token_id = result["token"]["id"]
    services = result["serviceCatalog"]
    for one in services:
        if one["name"] == "cinder":
            endpoints_list = one["endpoints"]
            for endpoint in endpoints_list:
                if endpoint.has_key("publicURL"):
                    url = endpoint["publicURL"]+"/volumes/detail?all_tenants=1"
                    
    headers = {'X-Auth-Token': token_id, 'User-Agent': 'python-novaclient' , 'Accept':'application/json','X-Auth-Project-Id':'admin'}
    result = json_request(url,'GET',data , headers)
    if result.has_key("volumes"):
        return result["volumes"]
    else:
        raise Exception("find volumes error")

   

def query_volumes(ip, username="admin", password="admin123"):
     

    result = _conn_keystone(ip, username, password)
    volumes = _query_volumes(result)
    volumes_dict = {}
    for v in volumes:
        volumes_dict[v["id"]]= v
            
        
    return volumes_dict
        
