import logging
import sys

# Создать логгер - регистратор верхнего уроовня
# с именем messenger.main
log = logging.getLogger('messenger.main')

# Создать обработчик
fh = logging.FileHandler("app_client.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG в файл app_client.log

# Создать объект Formatter
# Определить формат сообщений "дата время" "уровень важности" "имя модуля" "сообщение"
_format = logging.Formatter("%(asctime)s - %(levelname)s - $(module)s  - %(message)s ")

# подключить объект Formatter к обработчику
fh.setFormatter(_format)

# Добавить обработчик к регистратору
log.addHandler(fh)
log.setLevel(logging.DEBUG)

# Передать сообщение обработчику
log.info('Здесь будут логи клиентской части')
