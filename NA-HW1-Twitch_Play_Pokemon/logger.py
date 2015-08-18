#-*- encoding: utf-8 -*-
import time
import datetime
import keyholder
PLAYER_TOTAL={}
def getTimestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d %H:%M:%S')
def log(mode,user,myMsg):
    if user not in PLAYER_TOTAL and user != "":
        PLAYER_TOTAL[user] = 0
    if user in PLAYER_TOTAL:
        PLAYER_TOTAL[user] += 1
    if user not in keyholder.PLAYER and user != "":
        keyholder.PLAYER[user] = 0        
    record = '[%s] [%s] %s: %s [ %s / %s (exec/cmd)] ' % (getTimestamp(), mode, user, myMsg,keyholder.PLAYER[user],PLAYER_TOTAL[user])
#     print record
    fp = open("log", 'a')
    fp.write(record+"\n")
    fp.close()   
     
#     print keyholder.PLAYER
