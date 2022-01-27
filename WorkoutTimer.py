# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:47:48 2020
Workout App
@author: Thomas
"""
import winsound,time
frequency =500
duration =1000
ex=[]
item=''
i=0
while True:
    print("Adding Excersise. Press q to quit")
    item=input("What excersise will you add?: ")
    if item =='q':
        break
    ex.append(item)
    print(item, "has been added")
    


print("The excerises will begin in:")
for x in range (1,4):
    print(4-x)
    time.sleep(1)
for y in range(1,21):
    if i != int(len(ex)):
        print(ex[i])
        winsound.Beep(frequency,duration)
        time.sleep(29)
        print("Rest")
        winsound.Beep(1000,1000)
        time.sleep(29)
        i=i+1
    else:
        i=0
        print(ex[i])
        winsound.Beep(frequency,duration)
        time.sleep(29)
        print("Rest")
        winsound.Beep(1000,1000)
        time.sleep(29)
        i=i+1
print("End!")
winsound.Beep(1238,1000)
winsound.Beep(1312,1000)
winsound.Beep(1696,1000)