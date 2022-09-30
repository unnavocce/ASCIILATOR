from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import shutil
import time
import cv2
import os

path_to_video = str(input("Path to file: "))
vidcap = cv2.VideoCapture(path_to_video)
success, image = vidcap.read()
count = 0
path = str(input("Path to save: "))
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
        op += f'\nstring _{item.split(".",1)[0]} = @"\n{e}";'

with open(fr"{path}\final.txt","w") as f:
    f.write(op)