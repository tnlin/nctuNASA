import win32api
import win32con
import time
MSGCOUNT = {'up': 0, 'down': 0, 'right': 0, 'left': 0,          
          'a': 0, 'b': 0,'start': 0, 'select': 0}
MAP = {
    'up': 'i', 'down': 'k', 'right': 'l',  'left': 'j',
    'a': 'z',  'b': 'x','start': 'p', 'select': 'o'
}

VK_CODE = {'backspace':0x08,'enter':0x0D,
           'left':0x25,'up':0x26,'right':0x27,'down':0x28,
           'i':0x49,'j':0x4A,'k':0x4B,'l':0x4C,
           'o':0x4F,'p':0x50,'x':0x58,'z':0x5A
           }
PLAYER = {}
def holdForSeconds(key,seconds,user):
    if user not in PLAYER and user != "":
        PLAYER[user] = 0
    if user in PLAYER:
        PLAYER[user] += 1
    
    win32api.keybd_event(VK_CODE[MAP[key]], 0,0,0)
    time.sleep(seconds)
    win32api.keybd_event(VK_CODE[MAP[key]],0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(5*seconds)
    if key in MSGCOUNT:
        MSGCOUNT[key] += 1