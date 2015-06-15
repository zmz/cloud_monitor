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
            'timestamp': row['timestamp'].strftime('%Y-%m-%d'),
            'core': row['core'],
            'avg_core': row['avg_core'],
            'max': row['max'],
            'count': row['count'],
            'name': row['name']
        }
        result.append(record)

    return result

# rows = get_cpu('2015-06-08', '2015-06-20')
#
# print(json.dumps(rows))
# i = 0
# for row in rows:
#     i += 1
#     if i < 13:
#         print(row)
#         print(row['_id'], row['tenant_name'])