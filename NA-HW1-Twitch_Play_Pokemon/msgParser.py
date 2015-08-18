#-*- encoding: utf-8 -*-
class ParserHandler:
    KEYWORDS = ['up','down','right','left',
                'a','b','start','select']

    def __init__(self):
        pass

    def parser(self, message):
        ret = []
        while len(message) > 0:
            found = False
            for key in self.KEYWORDS:
                if message.find(key) == 0:
                    ret.append(key)
                    message = message[len(key):]
                    found = True
            if not found:
                message = message[1:]
        return ret