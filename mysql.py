#!/usr/bin/python

import MySQLdb

# connect
db = MySQLdb.connect(host="thinkman-wang.com", user="thinkman", passwd="Ab123456", db="db_thinknews")

cursor = db.cursor()
cursor.execute("SELECT * FROM user")
db.commit()

numrows = int(cursor.rowcount)
for x in range(0, numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1], "-->", row[2]
