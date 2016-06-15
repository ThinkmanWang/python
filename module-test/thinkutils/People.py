
class People:
    name=''
    age=0

    def __init__(self):
        self.name='Thinkman'
        self.age=32

    def toString(self):
        szRet = ("I'm %s. I'm %d year old" % (self.name, self.age))
        return szRet


