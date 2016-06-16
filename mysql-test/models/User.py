class User(object):
    id = 0
    user_name = ''
    password = ''
    
    def __init__(self, id=None, user_name=None, password=None):
        self.id = id
        self.user_name = user_name
        self.password = password
    