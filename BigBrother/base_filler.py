from deepface import DeepFace
import cv2
from main.models import *
import os
from pathlib import Path

import struct
import numpy as np
import json




def create_persona(name, image_path):

    embedding = DeepFace.represent(
        img_path=image_path,
        model_name="VGG-Face")

    # Создаем объект Persona

    mid = embedding[0]['embedding']
    json_embedding = json.dumps(mid)
    persona = Persona.objects.create(name=name, embedding=json.loads(json_embedding))
    print('Oki-Doki')

    return 0

for file in Path('C:/Users/Acer/OneDrive/Desktop/fs').glob('*.jpg'):
    name = file.stem  # Получаем имя файла без расширения
    image_path = str(file)  # Преобразуем путь в строку
    create_persona(name, image_path)