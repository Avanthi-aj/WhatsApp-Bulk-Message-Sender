from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")


# login_time = 10               
new_msg_time = 7            
send_msg_time = 3         
action_time = 2               
image_path ="C:/ragul.jpeg"
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://web.whatsapp.com')
input("Press ENTER...")

with open('message.txt', 'r',encoding='utf-8') as file:
    msg = file.read()

cnt=0
link = 'https://web.whatsapp.com'
driver.get(link)
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        try:
            num = n.rstrip()
            link = f'https://web.whatsapp.com/send/?phone={num}'
            driver.get(link)
            time.sleep(new_msg_time)
            attach_btn = driver.find_element(By.CLASS_NAME, '_1OT67')
            attach_btn.click()
            time.sleep(action_time)
            msg_input = driver.find_element(By.CLASS_NAME, '_1CGek input')
            msg_input.send_keys(image_path)
            time.sleep(action_time)
            actions = ActionChains(driver)
            for line in msg.split('\n'):
                actions.send_keys(line)
                actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(send_msg_time)
            cnt=cnt+1
            f=open("whatsapp_number.txt","a")
            f.write(num+'\n')
        except Exception as e:
            continue
f.close()
print(cnt)
driver.quit()
