class State:
    '''
    class Singleton.
    :param _state: Initialize the instance.
    :param fields: Dictionary.
    '''
    instance = None
    fields = {}

    def __new__(self, *args, **kwargs):
        if not self.instance:
            self.instance = super(State, self).__new__(self, *args, **kwargs)
        return self.instance