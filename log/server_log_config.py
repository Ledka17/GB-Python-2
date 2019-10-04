import logging
import sys

# Создать логгер - регистратор верхнего уроовня                                                                                  
# с именем messenger.main                                                                                                        
log = logging.getLogger('messenger.main')

# Создать обработчик                                                                                                             
fh = logging.FileHandler("app_server.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG в файл app_server.log                                                           

# Создать объект Formatter                                                                                                       
# Определить формат сообщений "дата время" "уровень важности" "имя модуля" "сообщение"                                           
_format = logging.Formatter("%(asctime)s - %(levelname)s - $(module)s  - %(message)s ")

# подключить объект Formatter к обработчику                                                                                      
fh.setFormatter(_format)

# Добавить обработчик к регистратору                                                                                             
log.addHandler(fh)
log.setLevel(logging.DEBUG)

# Передать сообщение обработчику                                                                                                 
log.info('Здесь будут логи серверной части')

#Создать ежедневную ротацию лог-файла

def create_rotating_log(path):
    #Создание ротацию лога
    logger = logging.getLogger('Rotating Log')

    #Устанавливаем уровень INFO
    logger.setLevel(logging.INFO)
 
    #Добавляем ротирующий handler
    handler = RotatingFileHandler('rot_app_server.log', maxBytes=20,
                                  backupCount=5, interval=86400)
    logger.addHandler(handler)
