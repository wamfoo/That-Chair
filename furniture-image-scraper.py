import os
import json 
import requests
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import time
import urllib.request

WAIT_TIME = 20
START, END = 1, 2
MAC_USER = "william"
MAC_DRIVER_PATH = f"/Users/{MAC_USER}/Downloads/chromedriver_mac_arm64/chromedriver"
SAVE_FOLDER = "furniture_images/"
GOOGLE_IMAGES = "https://www.google.com/search?q=furniture&client=safari&rls=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiuvs7CgND-AhWOTDABHUGWACQQ0pQJegQIAhAG&biw=1680&bih=945&dpr=2"


driver = webdriver.Chrome(MAC_DRIVER_PATH)
driver.maximize_window()
driver.implicitly_wait(WAIT_TIME)
driver.get(GOOGLE_IMAGES)

def wait_for_images_to_load():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rg_i")))
    print("Images loaded")

def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print("scrolling finished")

counter = 0
for i in range(START, END):     
    scroll_to_end()
    wait_for_images_to_load()
    image_elements = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    print(len(image_elements))
    for image in image_elements: 
        if (image.get_attribute("src") is not None):
            my_image = image.get_attribute("src").split("data:image/jpeg;base64,")
            filename = SAVE_FOLDER + "furtniture" + str(counter) + ".jpeg"
            if (len(my_image) > 1): 
                with open(filename, "wb") as f: 
                    f.write(base64.b64decode(my_image[1]))
            else: 
                print(image.get_attribute("src"))
                urllib.request.urlretrieve(image.get_attribute("src"), SAVE_FOLDER + "furniture" + str(counter) + ".jpeg")
            counter += 1


if __name__ == "__main__":
    pass