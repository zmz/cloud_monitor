__author__ = 'tianyuan8'

import pymongo
import datetime
import cfg


mongo_client = pymongo.MongoClient(cfg.MONGO_HOST, cfg.MONGO_PORT)
db = mongo_client[cfg.MOMGO_DATABASE]
if not db.authenticate(cfg.MONGO_DB_USER,cfg.MOMGO_DB_PASSWORD):
    raise Exception("Connect to mongodb error,please check user name and password!")
meter = db['meter']

def extract(time_begin, time_end, project_id):

    date_time_begin = datetime.datetime.strptime(time_begin,'%Y-%m-%d %H:%M')
    date_time_end = datetime.datetime.strptime(time_end,'%Y-%m-%d %H:%M')
    query = {"$and": [
                         {"timestamp": {"$gt": date_time_begin}},
                         {"timestamp": {"$lt": date_time_end}},
                         {"counter_name":
                              {"$in": ["cpu_util",
                                       "volume.write.bytes.rate",
                                       "volume.read.bytes.rate",
                                       "memory.usage",
                                       "network.incoming.bytes.rate",
                                       "network.outgoing.bytes.rate"
                                      ]
                               }
                          },
                         {"project_id": str(project_id)}
    ]}

    fields = {"counter_name": 1,
              "project_id": 1,
              #"user_id": 1,
              "resource_id": 1,
              "timestamp": 1,
              "resource_metadata.name": 1,
              "resource_metadata.instance_id": 1,
              "resource_metadata.display_name": 1,
              "resource_metadata.attachments.server_id": 1,
              #"counter_unit": 1,
              "counter_volume": 1,
             }

    #import time
    #t1 = time.time()
    cur = meter.find(query, fields).sort("timestamp")
    result = {}
    #t2 = time.time()
    #print str(t2-t1)
    for c in cur:
        if c["counter_name"] == "cpu_util":
            vm_id = c["resource_id"]
            if vm_id in result:
                if "cpu_util" in result[vm_id]:
                    result[vm_id]["cpu_util"]["timestamp"].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                else:
                    result[vm_id]["cpu_util"] = {"timestamp": [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])] ,
                                                 "counter_unit": "%"}
            else:
                result[vm_id] = {"cpu_util":{"timestamp": [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])],
                                             "counter_unit": "%"}}

        elif c["counter_name"] == "memory.usage":
            vm_id = c["resource_id"]
            if vm_id in result:
                if "memory" in result[vm_id]:
                    result[vm_id]["memory"]["timestamp"].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                else:
                    result[vm_id]["memory"] = {"timestamp": [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])] ,
                                                     "counter_unit": "MB"}
            else:
                result[vm_id] = {"memory":{"timestamp": [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])],
                                                 "counter_unit": "MB"}}

        elif c["counter_name"] == "volume.write.bytes.rate":
            vm_id = c["resource_metadata"]["attachments"][0]["server_id"]
            volume_display_name = c["resource_metadata"]["display_name"]
            if vm_id in result:
                if "volume_write" in result[vm_id]:
                    if volume_display_name in result[vm_id]["volume_write"]["volumes"]:
                        result[vm_id]["volume_write"]["volumes"][volume_display_name].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                    else:
                        result[vm_id]["volume_write"]["volumes"][volume_display_name] =[(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]
                else:
                    result[vm_id]["volume_write"] ={"volumes": {volume_display_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                              "counter_unit": "B/s"}
            else:
                result[vm_id] = {"volume_write":{"volumes": {volume_display_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                            "counter_unit": "B/s"}}
        elif c["counter_name"] == "volume.read.bytes.rate":
            vm_id = c["resource_metadata"]["attachments"][0]["server_id"]
            volume_display_name = c["resource_metadata"]["display_name"]
            if vm_id in result:
                if "volume_read" in result[vm_id]:
                    if volume_display_name in result[vm_id]["volume_read"]["volumes"]:
                        result[vm_id]["volume_read"]["volumes"][volume_display_name].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                    else:
                        result[vm_id]["volume_read"]["volumes"][volume_display_name] =[(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]
                else:
                    result[vm_id]["volume_read"]={"volumes": {volume_display_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                    "counter_unit": "B/s"}
            else:
                result[vm_id] = {"volume_read":{"volumes": {volume_display_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                              "counter_unit": "B/s"}}
        elif c["counter_name"] == "network.incoming.bytes.rate":
            vm_id = c["resource_metadata"]["instance_id"]
            tap_name = c["resource_metadata"]["name"]
            if vm_id in result:
                if "network_in" in result[vm_id]:
                    if tap_name in result[vm_id]["network_in"]["taps"]:
                        result[vm_id]["network_in"]["taps"][tap_name].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                    else:
                        result[vm_id]["network_in"]["taps"][tap_name] =[(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]
                else:
                    result[vm_id]["network_in"] = {"taps": {tap_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                                    "counter_unit": "B/s"}
            else:
                result[vm_id] = {"network_in": {"taps": {tap_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                                 "counter_unit": "B/s"}}
        elif c["counter_name"] == "network.outgoing.bytes.rate":
            vm_id = c["resource_metadata"]["instance_id"]
            tap_name = c["resource_metadata"]["name"]
            if vm_id in result:
                if "network_out" in result[vm_id]:
                    if tap_name in result[vm_id]["network_out"]["taps"]:
                        result[vm_id]["network_out"]["taps"][tap_name].append((c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"]))
                    else:
                        result[vm_id]["network_out"]["taps"][tap_name] =[(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]
                else:
                    result[vm_id]["network_out"] = {"taps": {tap_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                                    "counter_unit": "B/s"}
            else:
                result[vm_id] = {"network_out": {"taps": {tap_name: [(c["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),c["counter_volume"])]},
                                                                 "counter_unit": "B/s"}}
    #t3 = time.time()
    # print str(t3-t2)
    # sort_rst = {}
    for vm_id in result:
        if "volume_write" in result[vm_id]:
            volumes = result[vm_id]["volume_write"]["volumes"]
            result[vm_id]["volume_write"]["volumes"] = volumes.items()
        if "volume_read" in result[vm_id]:
            volumes = result[vm_id]["volume_read"]["volumes"]
            result[vm_id]["volume_read"]["volumes"] = volumes.items()
        if "network_out" in result[vm_id]:
            taps = result[vm_id]["network_out"]["taps"]
            result[vm_id]["network_out"]["taps"] = taps.items()
        if "network_in" in result[vm_id]:
            taps = result[vm_id]["network_in"]["taps"]
            result[vm_id]["network_in"]["taps"] = taps.items()

    return result

#project_id = "7b0a13d5d0d64a2998dc530acfbf2f08"
#result = extract(cfg.TIME_BEGIN, cfg.TIME_END, project_id)
#import json
#print json.dumps(result)

