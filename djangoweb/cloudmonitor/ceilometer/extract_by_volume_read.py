__author__ = 'tianyuan8'

import pymongo
import datetime
import cfg
from find_volumes import query_volumes
from find_vms import query_vm

COUNTER_NAME = "volume.read.bytes.rate"


mongo_client = pymongo.MongoClient(cfg.MONGO_HOST, cfg.MONGO_PORT)
db = mongo_client[cfg.MOMGO_DATABASE]
if not db.authenticate(cfg.MONGO_DB_USER,cfg.MOMGO_DB_PASSWORD):
    raise Exception("Connect to mongodb error,please check user name and password!")
meter = db['meter']
date_time_begin = datetime.datetime.strptime(cfg.TIME_BEGIN,'%Y-%m-%d %H:%M')
date_time_end = datetime.datetime.strptime(cfg.TIME_END,'%Y-%m-%d %H:%M')
query = {"$and": [
{"timestamp": {"$gt": date_time_begin}},
{"timestamp": {"$lt": date_time_end}},
{"counter_name": COUNTER_NAME}
#,{"resource_id": '4a864142-1079-4b15-b82a-0d3d510665e0'}
]}

result = {}
cur = meter.find(query)

for c in cur:
    c.pop("_id")
    c["timestamp"] = c["timestamp"].strftime('%Y-%m-%d %H:%M:%S')
    c["recorded_at"] = c["recorded_at"].strftime('%Y-%m-%d %H:%M:%S')
    if c["resource_id"] in result:
        result[c["resource_id"]]["list"].append(c)
        result[c["resource_id"]]["count"]= result[c["resource_id"]]["count"] +1
        result[c["resource_id"]]["max"] = c["counter_volume"] if (c["counter_volume"] > result[c["resource_id"]]["max"]) else result[c["resource_id"]]["max"]
        result[c["resource_id"]]["total"] = result[c["resource_id"]]["total"] + c["counter_volume"]
    else:
        result[c["resource_id"]] = {"list": [c], "count": 1, "max": c["counter_volume"], "total": c["counter_volume"],"node": [], "server": [], "display_name": ""}

print result




volumes = query_volumes(cfg.MANAGE_IP, cfg.USERNAME, cfg.PASSWORD)
vms = query_vm(cfg.MANAGE_IP, cfg.USERNAME, cfg.PASSWORD)
vm_dict = {}

for vm in vms:
    vm_dict[vm["id"]] = vm

for resource_id in result:
    if resource_id in volumes:
        volume = volumes[resource_id]
        result[resource_id]["display_name"] = volume["display_name"]
        for attach in volume["attachments"]:
            if attach["server_id"] in vm_dict:
                result[resource_id]["node"].append(vm_dict[attach["server_id"]]["OS-EXT-SRV-ATTR:host"])
                result[resource_id]["server"].append((attach["server_id"],vm_dict[attach["server_id"]]["name"]))
            else:
                result[resource_id]["server"].append((attach["server_id"],""))

for one in result:
    print result[one]