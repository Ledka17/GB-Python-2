from functools import wraps
import logging

# Функция log                                                                        
def log(logger):
    def wrap(func_log): # Функция декоратор
        @wraps(func_log) # Копирует атрибуты функции          
        def call(*args, **kwargs):
            return func_log(*args, **kwargs)
        return call
    return wrap

import logging
import sys

def func_log():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info(func_log.__doc__)

# Запись о функции декораторе
    _format = logging.Formatter("%(asctime)s функция %(funcName)s вызвана из функции %(funcModule)s") 

    fh.setFormatter(_format)

    log.addHandler(fh)
    log.setLevel(logging.DEBUG)
    log.info('Здесь будут логи клиентской части')

def main():
    call(func_log)

if __name__ == '__main__':
    main()
