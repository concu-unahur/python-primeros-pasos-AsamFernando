import logging
import threading

from operaNoConm import sumarUno
from operaNoConm import dividirPorDos
from operaNoConm import logResultado


logging.info('creando threads')
t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=dividirPorDos)
t3=threading.Thread(target=logResultado)

logging.info('comenzando thread 2 dividirPorDos')
t2.start()

logging.info('comenzando thread 1 SumarUno')
t1.start()

t3.start()