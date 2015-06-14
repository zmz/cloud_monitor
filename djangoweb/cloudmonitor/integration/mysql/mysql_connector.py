__author__ = 'zhangxg'

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('10.120.20.131', 'root', 'root', 'statistic');

    # cur = con.cursor()
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * from cpu_util")

    rows = cur.fetchall()

    for row in rows:
        print(row['_id'])

    # print "Database version : %s " % ver

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()