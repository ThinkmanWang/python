
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

print(sys.path)

from mysql_python import MysqlPython
from models.User import User

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
    