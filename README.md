# 2020PythonScripting
 Python Scripts which were to automate parts of work for the ECE Academic Continuity Team. Mostly outdated work, added to repo for documentation.
 These files are here for sstorage after difficulty finding them on previous work machines. Written using Spyder with a load of downloaded libraries at the recommendation of books 
 I was using as reference at the time.

 What each file is:
 CombinePDF: Uses PyPDF to combine PDFs as I was working offline and did not have access to tools which would let me combine PDFs. 
 EmailGrab: Uses PyAutoGUI and Selenium to webscrape emails of UBC ECE professors from a list. Was used to grab their contact information because we were unable
 to get a list of their emails and given the vast volume of professors at the univeristy, it would be very painful to email them all one by one.
 EmailSender: Uses PyAutoGUI and Pyperclip to send out a large volume of emails using the list of emails I got using EmailGrab. Unfortunately, the email client I had to
 use for work did not have a tool to do this, and it was on a web-based platform. The script would just iterate through the list and I had to add sleeps to prevent me 
 from outspeeding the server after my first tests sent blank emails.
 WebSiteSearch: Uses Selenium webdriver to search a bunch of different store websites for  items, used when purchasing for work and for personal use, especially since I was moving at the time.
 WorkoutTimer: A super basic bat file which let me customize HIIT workouts, mostly used because none of the apps I found met the type of workout I wanted to have. Since getting a smartwatch though, this hans't been as useful.'