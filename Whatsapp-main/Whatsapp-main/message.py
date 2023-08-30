from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=/home/username/.config/google-chrome")

driver = webdriver.Chrome(options=option)     

driver.get('https://web.whatsapp.com')
input("Press ENTER...")
with open('message.txt', 'r') as file:
    msg = file.read()

link = 'https://web.whatsapp.com'
driver.get(link)
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={num}'
        driver.get(link)
        time.sleep(10)
        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
driver.quit()
