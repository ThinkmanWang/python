#!/usr/bin/python

import MySQLdb
from utils.mysql_python import MysqlPython
from models.User import User
from utils.user_db_utils import *  
    
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
    
if __name__ == '__main__': 
    main();