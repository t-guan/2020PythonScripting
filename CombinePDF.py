# -*- coding: utf-8 -*-
"""
PDF Combiner
Created on Wed May 20 10:20:17 2020

@author: Thomas
"""
import PyPDF2, os, time
downloadstrue=str('C:\\Users\\Thomas\\Downloads')
while True:
    checklocation=str(input("Is the file located in Downloads? (Y/N): ")).upper()
    if checklocation == "Y":
        os.chdir(downloadstrue)
        break
    elif checklocation =="N":
        print("Please move the items into the downloads folder.")
        time.sleep(1)        
PDFs=[]
PDFNames={}
PDFRead={}
while True:
    try:
        Val=int(input("How many PDFs do you wish to combine?: "))
        while Val==0:
            print("You cannot combine zero PDFs. Please enter a valid integer")
            Val=int(input("How many PDFs do you wish to combine?: "))
        break
    except ValueError:
        print("Please input a number. Try again")
for i in range(0,Val):
    while True:
        try:
            Name=str(input("What is the name of the PDF?: "))
            Name=Name+'.pdf'
            break
        except ValueError:
            print("Please check the name agian")
    PDFs.append(Name)
for i in range(0,Val):
    try:
        PDFNames["PDF{0}".format(i)]=open(PDFs[i], 'rb')
        PDFRead["RPDF{0}".format(i)]=PyPDF2.PdfFileReader(PDFNames["PDF{0}".format(i)])
    except FileNotFoundError:
        print("These files are not in the file")
        print("Please check the names of your file and try again")
        time.sleep(5)
        exit()
writer = PyPDF2.PdfFileWriter()
for i in range(0,Val):
    for pageNum in range(PDFRead["RPDF{0}".format(i)].numPages):
        page=PDFRead["RPDF{0}".format(i)].getPage(pageNum)
        writer.addPage(page)
ComboName=str(input("What would you like to name your combined PDF?: "))
outFile=open(ComboName+'.pdf', 'wb')
writer.write(outFile)
outFile.close()

    
    

    
