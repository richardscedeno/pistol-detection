import os
import glob
import sys

sys.path.append('./telegram_bot')
from telegram_bot.bot import TelegramBot

bot = TelegramBot(properties_path='./telegram_bot/.telegram_keys')

# funcion para verificar el path donde se almacenan las detecciones en local, para poder enviar a telegram.
def verify_path():
    path = './runs/detect/'

    if os.path.exists(path):
        # verificamos la lista del directorios o entradas del path (lista de predicciones)
        predictions_list = os.listdir(path)
        # ordear la lista de directorios de predicciones
        predictions_list.sort()

        # ruta de las detecciones por defecto "./runs/detect/predict/crops/Gun"
        detection_path = f'{path}{predictions_list[-1]}/crops/Gun/'

        # verificar que la ruta de las detecciones existe
        if os.path.exists(detection_path):

            # obtener la lista de detecciones 
            detection_list = glob.glob(detection_path + '*.jpg')
            # Ordenamos para seleccionar la ultima
            detection_list.sort(key=os.path.getctime)
            
            # almacenamos la ultima deteccion
            last_detection = detection_list[-1]
            # descripcion para el envio a telegram
            description = 'Gun Detected' 

            # envio a telegram, con el bot creado.
            bot.send_photo_to_channel(last_detection, description)
          
verify_path()
