# exec(open('practice_deepface.py').read())

from deepface import DeepFace
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from main.models import *

def normalize(string):
    string = string[1: -1]
    result = [float(idx) for idx in string.split(', ')]
    return result
#
#
# chels = Persona.objects.all()
#
# first_embs = []
#
# try:
#     first_embs = DeepFace.represent(img_path = "C:/Users/Senpai/Videos/shredded_test/frame_0141.jpg", model_name = "VGG-Face")
# except ValueError:
#     print("Face not found")
#
# for chel in chels:
#     if len(first_embs) != 0:
#         result = DeepFace.verify(
#             img1_path=first_embs[0].get("embedding"),
#             img2_path=normalize(chel.embedding),
#             enforce_detection=False,
#             model_name="VGG-Face"
#         )
#         if result.get("verified"):
#             print(chel.name)
#             break




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


