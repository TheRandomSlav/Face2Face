from deepface import DeepFace
from main.models import Persona
import os
import django
from pathlib import Path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BigBrother.settings')
# django.setup()

def create_persona(name, image_path):

    embedding = DeepFace.represent(
        img_path=image_path,
        model_name="VGG-Face")

    # Создаем объект Persona
    persona = Persona.objects.create(name=name, embedding=embedding)

    print("Ready")
    return 0


for file in Path('C:/Users/Senpai/PycharmProjects/Face2Face/BigBrother/fs').glob('*.jpg'):
    name = file.stem  # Получаем имя файла без расширения
    image_path = str(file)  # Преобразуем путь в строку
    create_persona(name, image_path)