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
# from pyvirtualdisplay import Display
#
#
#
# display = Display(visible=1, size=(800, 600))
#display.start()

user = os.environ["USER"]
password = os.environ["PASSWORD"]
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-software-rasterizer')
options.binary_location="./webdriver/headless_shell"
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
        ### Define xpaths for buttons.
        first='//*[@id="content"]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/a'
        like='//*[@id="modal_content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div'
        xpf='//*[@id="copyrightTooltipContainer"]/div/div[2]'
        xpn='//*[@id="copyrightTooltipContainer"]/div/div[1]/div'

        driver.get('https://500px.com/fresh')
        time.sleep(5)
        ### Select first photo from fresh ###
        driver.find_element_by_xpath(first).click()
        time.sleep(5)
        ### Click like button ###
        driver.find_element_by_xpath(like).click()
        time.sleep(3)
        count=0
        while True:
                        i=0
                        for i in range(0,20):
                                ### Go to next photo. After first like xpath will be changed ###
                                if i >= 1:
                                    next=driver.find_element_by_xpath(xpf)
                                else:
                                    next=driver.find_element_by_xpath(xpn)
                                next.click()
                                time.sleep(2)
                                ###  Click like button ###
                                driver.find_element_by_xpath(like).click()
                                href=driver.current_url
                                i=i+1
                                count=count+1
                                print (count,  href)
                                time.sleep(1)
                        else:
                                driver.get('https://500px.com/fresh')
                                time.sleep(10)
                                ### Select first photo from fresh ###
                                driver.find_element_by_xpath(first).click()
                                time.sleep (2)
                                ### Click like button ###
                                driver.find_element_by_xpath(like).click()
                                time.sleep(2)
                                i=0

main ()
