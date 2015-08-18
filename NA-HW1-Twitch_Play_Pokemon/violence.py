#-*- encoding: utf-8 -*-
import datetime
import keyholder
import logger
from itertools import groupby
class ViolenceHandler:
    def __init__(self, delta,twitch):
        self.t = twitch
        self.mode = 'violence'
        self.last_time = datetime.datetime.now()
        self.time_delta = datetime.timedelta(seconds=delta)        
        self.count = {'up': 0,'down': 0,'left': 0,'right': 0,
                    'a': 0,'b': 0,'select': 0,'start': 0,
                    }
        self.temp = {'up': 0,'down': 0,'left': 0,'right': 0,
                    'a': 0,'b': 0,'select': 0,'start': 0,
                    }
    def set_time_delta(self, delta):
        self.time_delta = datetime.timedelta(seconds=delta)
    
    def clearTemp(self):
        for i in self.temp.keys():
            self.temp[i] = 0
                
    def clearCount(self):
        for i in self.count.keys():
            self.count[i] = 0

    def run(self, message,user):
        pre=""
        for m in message:
            if pre == m and m in self.temp.keys():
                self.temp[m] += 1                
            elif pre != m:
                self.temp[m] = 1
            pre = m
        _max = max(self.temp.values())
        for i in self.temp:
                if self.temp[i]==_max:
                    self.count[i]=self.temp[i]
        self.clearTemp()
        
        #if now - last > delta,then exec
        if datetime.datetime.now() - self.last_time >= self.time_delta:
            self.last_time = datetime.datetime.now()
            _max = max(self.count.values())            
            maxNum=0
            for i in self.count:
                if self.count[i]==_max:
                    maxNum += 1  
            #if maxOpion >= 2 , return 
            if maxNum>=2 and _max>0:                
                return      
            m = max(self.count.keys(), key=lambda x: self.count[x])            
            keyholder.holdForSeconds(m,0.05,"VIOLENCE");
            logger.log(self.mode,"VIOLENCE", m)            
            self.t.twitch_sendMsg(self.mode.upper()+":"+m.upper()) 
            self.clearCount()