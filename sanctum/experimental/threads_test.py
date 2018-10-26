from threading import Thread
import time
import threading

lock=threading.Lock()
net_data=[]
class every_sec(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = 0
 
 
    def run(self):
        while True:
            self.val+=5
            print('running ONE---------value====>',self.val)
            with lock:
                net_data.append(self.val)
            time.sleep(1)

class every_min(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = 0

    def run(self):
        while True:
            self.val+=60
            print('running MIN---------value====>',self.val)
            with lock:
                print('net stat at ',self.val,' : ', net_data)
                net_data.clear()
            time.sleep(5)
if __name__ == '__main__':
    es=every_sec()
    es.setName('second')
    em=every_min()
    es.setName('minute')


    es.start()
    em.start()

    es.join()
    em.join()

    print('main is gone...')