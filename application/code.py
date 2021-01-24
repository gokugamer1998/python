# Importing necessary packages 
import re
import PyPDF2
import requests
import pdfplumber
import pandas as pd
from collections import namedtuple
import sys
import pandas as pd

from tkinter import *
from tkinter.ttk import *
  
from tkinter.filedialog import askopenfile

import shutil 
import tkinter as tk
import tkinter as ts
from tkinter import messagebox, filedialog
import os


# Defining CreateWidgets() function to 
# create necessary tkinter widgets 
def CreateWidgets():

        """link_Label = Label(root, text ="Select The File To Copy : ",) 
        link_Label.grid(row = 1, column = 0, pady = 5, padx = 5)
    
        root.sourceText = Entry(root, width = 50, textvariable = sourceLocation) 
        root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2) """

        
	
        destinationLabel = Label(root, text ="Select The Destination : ")
        destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5) 
	
        root.destinationText = Entry(root, width = 50, textvariable = destinationLocation)
        root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5, columnspan = 2)
	
        dest_browseButton = Button(root, text ="Browse", command = DestinationBrowse, width = 15) 
        dest_browseButton.grid(row = 2, column = 3, pady = 5, padx = 5) 
	
        moveButton = Button(root, text ="Move File",command = MoveFile, width = 15) 
        moveButton.grid(row = 3, column = 2, pady = 5, padx = 5)

def open_pdf():
    file = askopenfile(mode ='rb', filetypes =[('Python Files', '*.pdf')])
    if file:	
        ap = pdfplumber.open(file)
        page = ap.pages[0]
        text = page.extract_text()
            
        
#-------------------------------------------------
        
    sys.stdout = open("test.txt", "w")
        
#-------------------------------------------
        
    print("1 , 2")
        
#-------------------------------------------
        
    for name in text.split('\n'):
            if "Facebook India Online Services Pvt. Ltd.," in name:
                name = name.replace(',', '')
                print("Name, "+ name)
#----------------------------------------------------------
    invoice = re.compile(r'  Invoice #: \d+')
    for invo in text.split('\n'):
            if invoice.match(invo):
                print("invno, "+invo[-10::])
#----------------------------------------------------------
    Invst = re.compile(r'Invoice Date: \d+')
    for invest in text.split('\n'):
            if Invst.match(invest):
                print("Invest   , "+invest[-11::])
#----------------------------------------------------------
    buyerGST = re.compile(r'GST Reg.No: \d+')
    for buyergst in text.split('\n'):
            if buyerGST.match(buyergst):
                print("Buyergst, "+buyergst[-15::])
#----------------------------------------------------------
    sellerGST = re.compile(r'GST: \d+')
    for sellergst in text.split('\n'):
            if sellerGST.match(sellergst):       
                print("SellerGST, "+sellergst[-15::].zfill(16))
#-----------------------------------------------------------
    for invamt in text.split('\n'):
        if "Invoice Total" in invamt:
                invamt = invamt.replace(',', '')
                print("InvAmt, "+invamt[-9::])
        
        
    sys.stdout.close()



    dataframe1 = pd.read_csv("test.txt")
    dataframe1.to_csv('final.csv', index = None)


file = r'D:\project\final.csv'

	
def DestinationBrowse(): 
	# Opening the file-dialog directory prompting 
	# the user to select destination folder to 
	# which files are to be copied using the 
	# filedialog.askopendirectory() method. 
	# Setting initialdir argument is optional 
	destinationdirectory = filedialog.askdirectory(initialdir ="D:\Series\Brooklyn Nine Nine") 

	# Displaying the selected directory in the 
	# root.destinationText Entry using 
	# root.destinationText.insert() 
	root.destinationText.insert('1', destinationdirectory) 
	
"""def CopyFile(): 
	# Retrieving the source file selected by the 
	# user in the SourceBrowse() and storing it in a 
	# variable named files_list 
	files_list = root.files_list 

	# Retrieving the destination location from the 
	# textvariable using destinationLocation.get() and 
	# storing in destination_location 
	destination_location = destinationLocation.get() 

	# Looping through the files present in the list 
	for f in files_list: 
		
		# Copying the file to the destination using 
		# the copy() of shutil module copy take the 
		# source file and the destination folder as 
		# the arguments 
		shutil.copy(f, destination_location) 

	messagebox.showinfo("SUCCESSFULL") """
	
def MoveFile(): 
	
	# Retrieving the source file selected by the 
	# user in the SourceBrowse() and storing it in a 
	# variable named files_list''' 
	#files_list = file

	# Retrieving the destination location from the 
	# textvariable using destinationLocation.get() and 
	# storing in destination_location 
	destination_location = destinationLocation.get() 

	# Looping through the files present in the list 
	#for f in file: 
		
		# Moving the file to the destination using 
		# the move() of shutil module copy take the 
		# source file and the destination folder as 
		# the arguments 
	shutil.move(file, destination_location) 

	messagebox.showinfo("SUCCESSFULL") 

# Creating object of tk class 
root = tk.Tk()
root1 = ts.Tk()
root.geometry('200x100')
	
# Setting the title and background color 
# disabling the resizing property 
root.geometry("830x120") 
root.title("Copy-Move GUI") 
root.config(background = "black") 
	
# Creating tkinter variable 
sourceLocation = StringVar() 
destinationLocation = StringVar() 
	
# Calling the CreateWidgets() function 
CreateWidgets()

btn = Button(root1, text ='Open', command = lambda:open_pdf())
btn.pack(side = TOP, pady = 10)
	
# Defining infinite loop 
root.mainloop() 
