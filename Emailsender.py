# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:41:38 2020

@author: Thomas
"""


import pyautogui, csv, time, pyperclip
ccemails='ignacio@ece.ubc.ca, maggiec@ece.ubc.ca'
#ccemails=''
subject='ECE Department Story Participation'
with open('AllEmails.csv') as csvfile:
    csvread=csv.reader(csvfile, delimiter=',')
    count=0
    for row in csvread:
        name=row[0]
        email=row[1]
        time.sleep(5)
        pyautogui.click(207, 460)
        time.sleep(3)
        pyautogui.click(803,602)
        pyautogui.write(email,interval=0.01)
        pyautogui.click(815,645)
        pyautogui.write(ccemails, interval=0.01)
        time.sleep(1)
        pyautogui.click(808,750)
        pyautogui.write(subject, interval=0.01)
        time.sleep(1)
        pyautogui.click(686,812, interval=0.25)
        pyautogui.click(688,857, interval=0.25)
        time.sleep(1)
        pyautogui.click(771,1183)
        pyautogui.write("Hello Captains of ")
        pyautogui.write(name+",", interval=0.01)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(15)
        pyautogui.click(243,468, interval=0.25)
        time.sleep(5)
        
        
