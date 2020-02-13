import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var1=1
semaforo=threading.Semaphore(1)


def sumarUno():
    global var1
    global semaforo
    try:
        var1+=1
    finally:
        semaforo.release()
        

def multiplicarPorDos():
    global var1
    global semaforo
    semaforo.acquire()
    try:
        var1*=2
    finally:
        semaforo.release()

semaforo.acquire()



t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=multiplicarPorDos)

t2.start()

t1.start()




t2.join()

logging.info(f'el resultado es: {var1}')