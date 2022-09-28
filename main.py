import time
from selenium import webdriver
from selenium import *
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import telebot
import cv2
import os
import shutil


bot = telebot.TeleBot("5645302503:AAEkj5QE1zosAt7exhjdZpfk83IbSVUCRcY")

@bot.message_handler(content_types=['video'])
def photo(message):
    fileID = message.video.file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"{message.from_user.id}.mp4", 'wb') as new_file:
      new_file.write(downloaded_file)
    new_file.close()
    vidcap = cv2.VideoCapture(f"{message.from_user.id}.mp4")
    success, image = vidcap.read()
    count = 0
    path = f"H:\Documents\scii\{message.from_user.id}"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    while success:
        cv2.imwrite(f"{path}\{count}.png", image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    test = os.listdir(path)
    width = 20
    op = ""
    for item in test:
        time.sleep(1)
        service_obj = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(15)
        driver.get('https://manytools.org/hacker-tools/convert-images-to-ascii-art/')
        element = driver.find_element(By.ID, "Form_go_ImgUpload")
        ActionChains(driver).send_keys(item).perform()
        element.send_keys(f"{path}\{item}")
        driver.find_element(By.ID, 'Form_go_Width').clear()
        driver.find_element(By.ID, 'Form_go_Width').send_keys(width)
        driver.find_element(By.ID, 'Form_go_action_Process').click()
        e = driver.find_element(By.CLASS_NAME, 'ascii').text
        #bot.send_message(message.chat.id, e)
        op += f'\nstring _{item.split(".",1)[0]} = @"\n{e}";'

    with open(fr"H:\Documents\scii\{message.from_user.id}\final.txt","w") as f:
        f.write(op)
    with open(fr"H:\Documents\scii\{message.from_user.id}\final.txt", "rb") as filee:

        bot.send_document(message.chat.id, filee)

bot.infinity_polling()









