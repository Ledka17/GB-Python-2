from functools import wraps

# Функция декоратор
def wrap(func_log):
    @wraps(func_log) # Копирует атрибуты функции (1 способ)
    def call(*args, **kwargs):
        return func_log(*args, **kwargs)
    call.__doc__ = func.__doc__ # Копирует имя и аргументы функции (2 способ)
    call.__name__ = func.__name__
    call.__dict__.update(func.__dict__)
    return call


import logging
import sys

def func_log():
    log = logging.getLogger('messenger.main')

    fh = logging.FileHandler("app_client.log", encoding='utf-8')

    _format = logging.Formatter("%(asctime)s - %(levelname)s - $(module)s  - %(message)s ")

    fh.setFormatter(_format)

    log.addHandler(fh)
    log.setLevel(logging.DEBUG)
    log.info('Здесь будут логи клиентской части')
