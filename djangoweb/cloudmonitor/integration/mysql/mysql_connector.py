__author__ = 'zhangxg'

import MySQLdb as mdb
import json
import datetime


config = {
    'ip': '10.120.20.131',
    'username': 'root',
    'password': 'root',
    'db_name': 'statistic'
}

connection = {}


def initialize_connection():
    global connection
    try:
        connection = mdb.connect(config['ip'], config['username'], config['password'], config['db_name'])
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    # finally:
    #     if connection:
    #         connection.close()


def get_cpu(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from cpu_util where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'tenant_id': row['tenant_id'],
            'vm_id': row['vm_id'],
            'tenant_name': row['tenant_name'],
            'count_unit': row['count_unit'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'core': row['core'],
            'avg_core': row['avg_core'],
            'max': row['max'],
            'count': row['count'],
            'name': row['name']
        }
        result.append(record)

    return result


def get_memory(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from memory_usage where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'tenant_id': row['tenant_id'],
            'vm_id': row['vm_id'],
            'tenant_name': row['tenant_name'],
            'count_unit': row['count_unit'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'ram': row['ram'],
            'avg_mem': row['avg_mem'],
            'max': row['max'],
            'rate': row['rate'],
            'count': row['count'],
            'name': row['name']
        }
        result.append(record)

    return result


def get_disk_read(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from disk_read where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'resource_id': row['resource_id'],
            'display_name': row['display_name'],
            'vm_id': row['vm_id'],
            'vm_name': row['vm_name'],
            'tenant_id': row['tenant_id'],
            'tenant_name': row['tenant_name'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'count_unit': row['count_unit'],
            'avg_read': row['avg_read'],
            'max_read': row['max_read'],
            'count': row['count']
        }
        result.append(record)

    return result


def get_disk_write(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from disk_write where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'resource_id': row['resource_id'],
            'display_name': row['display_name'],
            'vm_id': row['vm_id'],
            'vm_name': row['vm_name'],
            'tenant_id': row['tenant_id'],
            'tenant_name': row['tenant_name'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'count_unit': row['count_unit'],
            'avg_write': row['avg_write'],
            'max_write': row['max_write'],
            'count': row['count']
        }
        result.append(record)

    return result


def get_network_in(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from network_in where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'resource_id': row['resource_id'],
            'tap_name': row['tap_name'],
            'vm_id': row['vm_id'],
            'vm_name': row['vm_name'],
            'tenant_id': row['tenant_id'],
            'tenant_name': row['tenant_name'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'count_unit': row['count_unit'],
            'avg_in': row['avg_in'],
            'max_in': row['max_in'],
            'count': row['count']
        }
        result.append(record)

    return result


def get_network_out(date_start, date_end):
    if not connection:
        initialize_connection()

    cursor = connection.cursor(mdb.cursors.DictCursor)
    sql_string = 'select * from network_out where timestamp between \'' + date_start + '\' and \'' + date_end + '\''
    cursor.execute(sql_string)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        record = {
            'id': row['_id'],
            'resource_id': row['resource_id'],
            'tap_name': row['tap_name'],
            'vm_id': row['vm_id'],
            'vm_name': row['vm_name'],
            'tenant_id': row['tenant_id'],
            'tenant_name': row['tenant_name'],
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'count_unit': row['count_unit'],
            'avg_out': row['avg_out'],
            'max_out': row['max_out'],
            'count': row['count']
        }
        result.append(record)

    return result


# disk_r = get_disk_read('2015-06-08', '2015-06-20')
# print(disk_r.__len__())
# disk_w = get_disk_write('2015-06-08', '2015-06-20')
# print(disk_w.__len__())
#
# net_in = get_network_in('2015-06-08', '2015-06-20')
# print(net_in.__len__())
# net_out = get_network_out('2015-06-08', '2015-06-20')
# print(net_out.__len__())


# r = get_memory('2015-06-08', '2015-06-20')
# print(json.dumps(r))
# i = 0
# for row in rows:
#     i += 1
#     if i < 13:
#         print(row)
#         print(row['_id'], row['tenant_name'])