#/usr/bin/env python
#coding=utf-8

import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
        
    def run(self):
        apply(self.func,self.args)
        
def super_play(file,time):
    for i in range(2):
        print 'Starting playing: %s! %s'%(file,ctime())
        sleep(time)
        
list={'Star':2,'Man':4,'XX':6}

threads=[]
files=range(len(list))

for k,v in list.items():
    t=MyThread(super_play,(k,v),super_play.__name__)
    threads.append(t)
    
if __name__=='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
        
    print 'end playing %s!'%ctime()
