from deepface import DeepFace
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from main.models import *

chels = Persona.objects.all()

for chel in chels:
    print(chel.name)

#
# def open_file():
#   # Создаем экземпляр Tkinter
#   root = tk.Tk()
#   root.withdraw()  # Скрываем главное окно
#
#   # Открываем диалоговое окно для выбора файла
#   file_path = filedialog.askopenfilename()
#
#   return file_path
#
#
# img1 = open_file()
# img2 = open_file()
#
#
# img1_embs = DeepFace.represent(img_path = img1, model_name = "VGG-Face")
# img2_embs = DeepFace.represent(img_path = img2, model_name = "VGG-Face")
#
# result = DeepFace.verify(
#   img1_path = img1_embs[0].get("embedding"),
#   img2_path = img2_embs[0].get("embedding"),
#   model_name="VGG-Face"
# )
#
# # result = DeepFace.verify(
# #   img1_path = img1,
# #   img2_path = img2,
# #   model_name="VGG-Face"
# # )
#
# print(result)
# verification = result.get("verified")
#
# if verification:
#   print(" Это один человек")
# else:
#   print("Это разные люди")
#
# print(img1_embs[0].get("embedding"))
# print(img2_embs)


