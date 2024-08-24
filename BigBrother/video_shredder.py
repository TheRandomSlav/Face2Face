# exec(open('video_shredder.py').read())

import cv2
import os
import tkinter as tk
from tkinter import filedialog
from main.models import *
from deepface import DeepFace


def normalize(string):
    string = string[1: -1]
    result = [float(idx) for idx in string.split(', ')]
    return result


def identify_face(frame):
    chels = Persona.objects.all()

    try:
        first_embs = DeepFace.represent(img_path=frame,
                                        model_name="VGG-Face")
    except ValueError:
        print("Face not found")
        return "no face"

    for chel in chels:
        if len(first_embs) != 0:
            result = DeepFace.verify(
                img1_path=first_embs[0].get("embedding"),
                img2_path=normalize(chel.embedding),
                enforce_detection=False,
                model_name="VGG-Face"
            )
            if result.get("verified"):
                return chel.name


def open_file():
  # Создаем экземпляр Tkinter
  root = tk.Tk()
  root.withdraw()  # Скрываем главное окно

  # Открываем диалоговое окно для выбора файла
  file_path = filedialog.askopenfilename()

  return file_path


def clear_directory(filepath):
    try:
        files = os.listdir(filepath)
        for file in files:
            file_path = os.path.join(filepath, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")


# faces = Persona.objects.all()

video_path = "C:/Users/Senpai/Videos/faces.mp4"
output_folder = 'C:/Users/Senpai/Videos/shredded_test'  # Замените на путь к вашей папке

# Создаем папку для сохранения кадров, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Загружаем видео с помощью OpenCV
cap = cv2.VideoCapture(video_path)

# Проверяем, удалось ли открыть видео
if not cap.isOpened():
    print("Не удалось открыть видео.")
    exit()

frame_count = 0
clear_directory("C:/Users/Senpai/Videos/shredded_test")

# Читаем кадры из видео
while True:
    ret, frame = cap.read()

    if not ret:
        # Когда кадры закончились
        break

    identify = identify_face(frame)
    if identify == "no face":
        continue
    else:
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}_{identify}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Frame Saved {frame_count} в {frame_filename}")

    frame_count += 1

# Освобождаем ресурс видео
cap.release()
print("All frames processed.")