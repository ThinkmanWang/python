#!/usr/bin/python
#coding=utf-8

import MySQLdb
from utils.mysql_python import MysqlPython
from models.User import User
from utils.user_db_utils import *  
import json
from utils.object2json import obj2json
    
def main():
    print 'Hello World'  
    myDB = MysqlPython('thinkman-wang.com', 'thinkman', 'Ab123456', 'db_thinknews')
    
    szSql = 'select * from user'
    result = myDB.select_advanced(szSql)

    for obj in result :
        user = User()
        user.id, user.user_name, user.password = obj
        
        print("%d | %s | %s" % (user.id, user.user_name, user.password))
    
    lstUser = get_all_users()
    for user in lstUser :
        print("%d | %s | %s" % (user.id, user.user_name, user.password))
        
    lstUser = get_all_user_from_pool();
    for user in lstUser :
        print("%d | %s | %s" % (user.id, user.user_name, user.password))    
            
    lstUser = get_all_user_from_pool();
    for user in lstUser :
        print("%d | %s | %s" % (user.id, user.user_name, user.password))
    
    lstUser = get_all_user_from_pool();
    for user in lstUser :
        print("%d | %s | %s" % (user.id, user.user_name, user.password))   
    
    print obj2json(lstUser)
    
if __name__ == '__main__': 
    main();