import threading 
import time 
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir():
    logging.info('Empezando desde funcion')
    time.sleep(1)
    logging.info('finalizando desde funcion')

t1 = threading.Thread(target=dormir, name='thread desde funcion')


class Unthread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name='threadClase'
    def run(self):
        logging.info('Empezando desde clase')
        time.sleep(1)
        logging.info('finalizando desde clase')

t2=Unthread()

t2.start()
t1.start()