# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:18:34 2020

@author: Thomas
"""
import time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
emails_list=[]
email_list=[]
driver =webdriver.Chrome(ChromeDriverManager().install())
file=open("professors.txt", "r")
members=file.readlines()
for prof in members:
    driver.get("https://www.google.ca")
    que=driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(f"UBC ECE {prof}")
    try:
        que.send_keys(Keys.RETURN)
    except Exception:
        pyautogui.click(902,684)
        time.sleep(3)
        email=driver.find_elements_by_class_name('spamspan')
        time.sleep(3)
        try:
            name=driver.find_element_by_class_name("node").find_element_by_tag_name("h3").text
            emails_list.append(name)
        except Exception:
            None
    for i in email:
        emails_list.append(i.text)
        
            #%%
for i in email_list:
    emails_list.append(i.text)
    

#%%
file=open("emails.txt","w")
for i in emails_list:
    file.write(i)
    file.write('\n')
file.close()

    
    

