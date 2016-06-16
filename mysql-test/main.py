#!/usr/bin/python

import MySQLdb
from utils.mysql_python import MysqlPython
from models.User import User

if __name__ == '__main__':  
    print 'Hello World'  
    myDB = MysqlPython('thinkman-wang.com', 'thinkman', 'Ab123456', 'db_thinknews')
    
    szSql = 'select * from user'
    result = myDB.select_advanced(szSql)

    for obj in result :
        user = User()
        user.id, user.user_name, user.password = obj
        
        print("%d | %s | %s" % (user.id, user.user_name, user.password))
        