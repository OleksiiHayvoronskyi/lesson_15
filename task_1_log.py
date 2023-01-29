from datetime import datetime
import socket

import logging
import logging.config
import time
import os

# Завдання 1. Використовуючи код з дом. завдання 1 лекції 11,
# додайте до сервера чата систему логувування рівня INFO, WARRING та ERROR.


print('--- Task 1 ---')

# read initial config file
logging.config.fileConfig('logging.conf')

# create and start listener on port 9999
t = logging.config.listen(60000)
t.start()

logger = logging.getLogger('simpleExample')

try:
    # loop through logging calls to see the difference
    # new configurations make, until Ctrl+C is pressed
    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(5)
except KeyboardInterrupt:
    # cleanup
    logging.config.stopListening()
    t.join()

# СЕРВЕР

print('--- Task 1. TCP Server ---')

address = ('localhost', 60000)
max_size = 1024

print('Server has been started at', datetime.now())
print('Server is waiting on a client...')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

conn, addr = server.accept()
print('Connected with:', addr)
data = conn.recv(max_size)
print(f'Client {addr} at', datetime.now(), 'said:', data)
# print('At', datetime.now(), conn, 'said', data)
conn.sendall(b'Do you want to talk with me?'.upper())

conn.close()
server.close()