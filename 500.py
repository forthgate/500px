#!/usr/bin/env python3

####################################################################################
##                                                                                ##
##                             500px PROMOTION SCRIPT                             ##
##                 This is my first script on Python, so if you have              ##
##          some questions or suggestion contact me to forthgate@gmail.com        ##
##                                                                                ##
####################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

user = os.environ["USER"]
password = os.environ["PASSWORD"]
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome (executable_path='./webdriver/chromedriver', options=options)


def login ():
        driver.get('https://500px.com/login')
        email = driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(str(user))
        passwd = driver.find_element_by_xpath('//*[@id="password"]')
        passwd.send_keys(str(password))
        passwd.send_keys(Keys.RETURN)
        time.sleep (3)

login ()

def main ():
        driver.get('https://500px.com/fresh')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="modal_content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div').click()
        time.sleep(3)
        count=0
        while True:
                try:
                        i=0
                        while i <20:
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="copyrightTooltipContainer"]/div[1]/div[1]').click()
                                time.sleep(2)
                                url=driver.find_element_by_xpath('//*[@id="modal_content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div')
                                url.click()
                                href=driver.current_url
                                i=i+1
                                count=count+1
                                print (count,  href)
                except:
                                driver.get('https://500px.com/fresh')
                                time.sleep(5)
                                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/a').click()
                                time.sleep (2)
                                driver.find_element_by_xpath('//*[@id="modal_content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div').click()
                                time.sleep(7)
                                i=0
                                continue
main ()
