from deepface import DeepFace
import cv2
import os
import tkinter as tk
from tkinter import filedialog


def open_file():
  # Создаем экземпляр Tkinter
  root = tk.Tk()
  root.withdraw()  # Скрываем главное окно

  # Открываем диалоговое окно для выбора файла
  file_path = filedialog.askopenfilename()

  return file_path


img1 = open_file()
img2 = open_file()

result = DeepFace.verify(
  img1_path = img1,
  img2_path = img1,
)

verification = result.get("verified")

if verification:
  print("Это один человек")
else:
  print("Это разные люди")