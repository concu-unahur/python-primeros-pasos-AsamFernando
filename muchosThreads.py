import threading
import time
import logging
from dormilones import Contador


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cont=Contador()

# la función para usar para el thread
def dormir(segs):
    time.sleep(segs)

logging.info('iniciando contador')
cont.iniciar()

logging.info('creando threads')

threadList=[]

for i in range(5): # arranca todos lo threads al mismo tiempo
    #crear un thread
    threadX=threading.Thread(target=dormir, args=[1], name='hilo')
    threadX.start()
    threadList.append(threadX)

for i in threadList:# este for espera casi al mismo tiempo todos los threads lanzados
    i.join()

cont.finalizar()
cont.imprimir()