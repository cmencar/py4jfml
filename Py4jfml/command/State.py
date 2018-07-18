#class Singleton:
class Singleton(object):

    _instance = None
    _str = ''

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self, *args, **kwargs)
        return self._instance

    def setStrXml(self, str):
        self._str = str

    def getStrXml(self):
        return self._str