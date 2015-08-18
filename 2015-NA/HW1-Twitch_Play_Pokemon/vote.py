#-*- encoding: utf-8 -*-
import datetime
import logger
class VoteHandler:
    def __init__(self, delta,twitch):        
        self.t = twitch        
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)
        self.count = {'democracy': 0,'normal': 0,'violence': 0, 'reverse': 0,}

    def set_time_delta(self, delta):
        self.time_delta = datetime.timedelta(seconds=delta)
    
    def clearCount(self):
        for i in self.count.keys():
            self.count[i] = 0

    def run(self, m ,user,mode):
        self.mode = mode
        self.count[m] += 1
        if datetime.datetime.now() - self.last_time >= self.time_delta:
            self.last_time = datetime.datetime.now()
            _max = max(self.count.values())
            #if maxOpion >= 2
            maxNum=0
            for i in self.count:
                if self.count[i]==_max:
                    maxNum += 1  
            if maxNum>=2 and _max>0:
                for i in self.count:
                    if self.count[i] != _max:
                        self.count[i] = 0 # reset                
                return
            if _max > 0:            
                m = max(self.count.keys(), key=lambda x: self.count[x])          
                logger.log(self.mode, "CHMOD", m)
                self.t.twitch_sendMsg("CHMOD:[ %s ]" % (str)(m).upper())
                self.clearCount()
                self.mode = m
            return self.mode
