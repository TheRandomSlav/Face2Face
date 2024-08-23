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


video_path = open_file()
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

# Читаем кадры из видео
while True:
    ret, frame = cap.read()

    if not ret:
        # Когда кадры закончились
        break

    # Сохраняем каждый кадр в папке
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"Сохранен кадр {frame_count} в {frame_filename}")

    frame_count += 1

# Освобождаем ресурс видео
cap.release()
print("Все кадры сохранены.")