#-*- encoding: utf-8 -*-
import datetime
import keyholder
import logger
class DemocracyHandler:
    def __init__(self, delta,twitch):
        self.t = twitch
        self.mode = "democracy"
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)
        self.count = {'up': 0,'down': 0,'left': 0, 'right': 0,
                      'a': 0,'b': 0,'select': 0,'start': 0,
                      }

    def set_time_delta(self, delta):
        self.time_delta = datetime.timedelta(seconds=delta)
    
    def clearCount(self):
        for i in self.count.keys():
            self.count[i] = 0

    def run(self, message,user):
        for m in message:
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
                        self.count[i] = -1000 # reset                
                return            
            m = max(self.count.keys(), key=lambda x: self.count[x])          
            keyholder.holdForSeconds(m,0.05,"DEMOCRACY");
            logger.log(self.mode, "DEMOCRACY", m)
            self.t.twitch_sendMsg(self.mode.upper()+":"+m.upper()) 
            self.clearCount()

