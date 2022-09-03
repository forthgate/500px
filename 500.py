#!/usr/bin/env python3

####################################################################################
##                                                                                ##
##                         500px SELF PROMOTION SCRIPT                            ##
##                 This is my first script on Python,if you have                  ##
##          some questions or suggestions contact me to forthgate@gmail.com       ##
##                                                                                ##
####################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import os

user = os.environ["USER"]
password = os.environ["PASSWORD"]
options = Options()
#options.headless = True
#options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

### Define xpaths for buttons.
pswd='//*[@id="password"]'
first='//*[starts-with(@id, "photo-")]/a'
like='//*[@id="open-modal"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div'
xpf='//*[@id="copyrightTooltipContainer"]/div/div/div[3]/div[2]/div/div'
xpn='//*[@id="copyrightTooltipContainer"]/div[1]/div/div[3]/div/div/div'
scauth='//*[@id="root"]/div[2]/div[1]/nav/a[3]'

def wdw(xpath):
    wdw=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath )))

def login ():
        driver.get('https://web.500px.com/login')
        wdw(pswd)
        email = driver.find_element("xpath",'//*[@id="emailOrUsername"]')
        email.send_keys(str(user))
        passwd = driver.find_element("xpath",pswd)
        passwd.send_keys(str(password))
        passwd.send_keys(Keys.RETURN)
        wdw(scauth)
        
login ()

def main ():
        driver.get('https://500px.com/fresh')
        wdw(first)
        ### Select first photo from fresh ###
        driver.find_element("xpath",first).click()
        ### Click like button ###
        driver.find_element("xpath",like).click()
        count=0
        while True:
                        i=0
                        for i in range(0,20):
                                ### Go to next photo. After first like xpath will be changed ###
                                if i >= 1:
                                    next=driver.find_element("xpath",xpf)
                                else:
                                    next=driver.find_element("xpath",xpn)
                                next.click()
                                ###  Click like button ###
                                driver.find_element("xpath",like).click()
                                href=driver.current_url
                                i=i+1
                                count=count+1
                                print (count,  href)
                                time.sleep(3)
                        else:
                                driver.get('https://500px.com/fresh')
                                wdw(first)
                                ### Select first photo from fresh ###
                                driver.find_element("xpath",first).click()
                                ### Click like button ###
                                driver.find_element("xpath",like).click()
                                i=0

main ()
