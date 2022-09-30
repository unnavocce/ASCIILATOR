from PIL import Image
import numpy as np
import shutil
import texts
import math
import os


def start():
    print(texts.greeting_message)
    input_processing()


def input_processing():
    user_input = str(input())
    user_input_splitted = user_input.split(" ")
    print(user_input_splitted[3][:3])
    if user_input_splitted[0] == "ascii" and user_input_splitted[1][0] == "-" \
            and user_input_splitted[2][:2] == "--" \
            and user_input_splitted[3][:3] == "-s":
        file_path = user_input_splitted[1][1::]
        folder_path = user_input_splitted[2][2::]
        mode = user_input_splitted[3][3::]
        print(file_path, folder_path, mode)
        if file_path[-3:] == "mp4":
            mp4_to_frames(file_path, folder_path)
        elif file_path[-3:] == "gif":
            gif_to_frames(file_path, folder_path)
        else:
            error()
    elif user_input_splitted[0] == "ascii":
        start()

    else:
        error()


def mp4_to_frames(to_mp4: str, to_folder: str):
    import cv2
    try:
        if os.path.exists(to_folder):
            shutil.rmtree(to_folder)
        os.mkdir(to_folder)
    except Exception(PermissionError):
        print("[PERMISSION ERROR] Try another directory")
    vidcap = cv2.VideoCapture(to_mp4)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"{to_folder}\{count}.png", image)
        success, image = vidcap.read()
        count += 1
    frames_to_ascii()

def gif_to_frames(to_gif: str, to_folder: str):
    if os.path.exists(to_folder):
        shutil.rmtree(to_folder)
    os.mkdir(to_folder)
    imageObject = Image.open(to_gif)
    for frame in range(0, imageObject.n_frames):
        imageObject.seek(frame)
        imageObject.save(fr"{to_folder}\{frame}.png")
    frames_to_ascii()

def frames_to_ascii(to_folder:str, width:int, cols:int):
    test = os.listdir(to_folder)
    width = 20
    op = ""
    gscale = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    for item in test:
        return

def output():
    return


def error():
    print("[ERROR] Please, enter your request again")
    start()


if __name__ == "__main__":
    start()
