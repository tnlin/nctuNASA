#-*- encoding: utf-8 -*-my
#Define the imports
import twitch
import keyholder
import os
import sys
import logger
from msgParser import ParserHandler
from democracy import DemocracyHandler
from violence import ViolenceHandler
from vote import VoteHandler
#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
broadcaster = ""
key = ""
#
p = ParserHandler()
t = twitch.Twitch()
t.twitch_connect(broadcaster, key)
d = DemocracyHandler(3,t)
v = ViolenceHandler(3,t)
vot = VoteHandler(10,t)
mode = "normal"
MODES = ['democracy', 'normal' , 'violence','reverse']
KEYWORDS = ['up','down','right','left',
            'a','b','start','select']
REVERSE = {
    'up': 'down', 'down': 'up', 'right': 'left',  'left': 'right',
    'a': 'b',  'b': 'a','start': 'select', 'select': 'start'
}
#The main loop
while True:
    os.system('cls')
    print('\n')
    sys.stdout.write("\t"+mode.upper()+ " MODE")
    sys.stdout.flush()
    #Check for new mesasages
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        #No new messages...
        continue
    else:
        for message in new_messages:
            #Wuhu we got a message. Let's extract some details from it
            user = message['username'].lower()
            msg = message['message'].lower()            
            #Broadcaster Only CMD
            if user == broadcaster and msg in MODES: 
                    text = "CHMOD:[ %s ]" % (str)(msg).upper()
                    t.twitch_sendMsg(text)                                 
                    logger.log(mode,user,text)
                    mode = msg
            elif msg in MODES:
                vot.run(msg, user,mode)
            elif user == broadcaster and msg =="!player":                
                t.twitch_sendMsg((str)(keyholder.PLAYER))
            elif user == broadcaster and msg =="!counter":                
                t.twitch_sendMsg((str)(keyholder.MSGCOUNT))                
            else:            
                #Switch by Mode
                msgList = p.parser(msg)                
                if mode == "normal":                       
                    for m in msgList:
                        keyholder.holdForSeconds(m,0.05,user);                                                                      
                if mode == "democracy":    
                    d.run(msgList,user)  
                if mode == "violence":                       
                    v.run(msgList,user)
                if mode == "reverse":
                    for m in msgList:
                        keyholder.holdForSeconds(REVERSE[m],0.05,user);
                logger.log(mode,user,msg) 
