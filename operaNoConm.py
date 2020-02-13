import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var1=1
lock= threading.Lock()

def dormir():
    time.sleep(1)

def sumarUno():
    global var1
    global lock
    try:
        var1+=1
    finally:
        lock.release()

def multiplicarPorDos():
    global var1
    global lock
    lock.acquire()
    try:
        var1*=2
    finally:
        lock.release()

def dividirPorDos():
    global var1
    global lock
    lock.acquire()
    try:
        var1/=2
    finally:
        lock.release()

lock.acquire()

t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=multiplicarPorDos)

t2.start()
t1.start()

#t2.join()

logging.info(f'el resultado es: {var1}')

#t1.join()
#t2.join()

'''def logResultado():
    lock.acquire()
    try:
        logging.info(f'el resultado es: {var1}')
    finally:
        lock.release()'''


