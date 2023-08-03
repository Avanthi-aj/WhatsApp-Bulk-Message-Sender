from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os


chrome_driver_path = ChromeDriverManager().install()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()



wh_number=[]
not_send=[]
numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number=len(numbers)
delay = 7

f=open("whatsapp_number.txt","w")
driver.get('https://web.whatsapp.com')
input("Press ENTER...")
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number) )
    try:
        url = f'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        if not sent:
            driver.get(url)
            try:
                click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
            except Exception as e:
                print(f"\nFailed to send message to: {number}")
                not_send.append(number)
            else:
                sleep(1)
                click_btn.click()
                sent=True
                sleep(1)
                print('Message sent to: ' + number)
                wh_number.append(number)
                f.write(number)
                f.write("\n")
    except Exception as e:
        print('Failed to send message to 1 ' + number + str(e))
        not_send.append(number)
print(wh_number)
print(not_send)
driver.close()
