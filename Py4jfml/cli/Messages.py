msg = {'FileNotFoundError':'A file isn\'t found', 'IOError':'A file is empty', 'IndexError':'Wrong number of arguments in Evaluate', 'NameError':'A file haven\'t the correct extension', 'NoOption':'Wrong or missing option', 'OnlyLoad':'Can\'t be executed only Load', 'ValueError':'Values must be Integer or Float in Evaluate'}

def getMsg(key):
    '''
    Return the message of the key in input
    :param key: key of the message
    '''
    assert type(key) == str
    return msg[key]