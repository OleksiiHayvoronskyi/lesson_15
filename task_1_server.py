from datetime import datetime
import socket
import logging

# Завдання 1. Використовуючи код з дом. завдання 1 лекції 11,
# додайте до сервера чату систему логувування рівня INFO, WARRING та ERROR.

# СЕРВЕР

print('--- Task 1. TCP Server ---')

# Створюю логер
module_logger = logging.getLogger('logging.task_1_server')


# Функція сервера.
def get_serv():
    address = ('localhost', 60000)
    max_size = 1024

    logger = logging.getLogger('logging.task_1_server')
    module_logger.info('Server has been started')
    logger.info(f'Connection with address {address}')
    logger.warning('This is a warn message')
    logger.error('This is an error message')
    logger.info('Server is waiting on a client...')

    print('Server has been started at', datetime.now())
    print('Server is waiting on a client...')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(address)

    server.listen(5)

    conn, addr = server.accept()
    print('Connected with:', addr)
    data = conn.recv(max_size)
    print(f'Client {addr} at', datetime.now(), 'said:', data)

    conn.sendall(b'Do you want to talk with me?'.upper())

    conn.close()
    server.close()


# Запускаю сервер.
get_serv()
