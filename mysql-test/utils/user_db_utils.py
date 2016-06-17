
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

print(sys.path)

from mysql_python import MysqlPython
from models.User import User
import mysql.connector.pooling.MySQLConnectionPool

def get_all_users() :
    myDB = MysqlPython('thinkman-wang.com', 'thinkman', 'Ab123456', 'db_thinknews')
    
    szSql = 'select * from user'
    result = myDB.select_advanced(szSql)

    lstUser = []
    for obj in result :
        user = User()
        user.id, user.user_name, user.password = obj
        lstUser.append(user)
        
    return lstUser


dbconfig = {
    "host": "thinkman-wang.com"
    , "database": "db_thinknews"
    , "user": "thinkman"
    , "password": "Ab123456"
}
        
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 3, **dbconfig)

def get_all_user_from_pool():
    conn = cnxpool.get_connection()
    cursor = conn.cursor();
    cursor.execute("select * from user");    
    list = cursor.fetchall();
    
    
    