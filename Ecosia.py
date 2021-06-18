# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
#import pandas as pd
import urllib.request
#from requests import get

from bs4 import BeautifulSoup
#import os
#import csv
#import requests
import sys

#import re
import xlsxwriter
#import pandas as pd
#import openpyxl
#import xlwt






#Scraping of the number of trees
# Lien de la page à scraper
urlpage = "https://info.ecosia.org/"
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page)
#print(soup.prettify())

match = soup.find('div',class_='statistics-item statistics-item-central hidden-desktop')
treecount=match.b.text
treecount = ''.join(str(elem) for elem in treecount)
treecount= treecount.replace(',','')
print(treecount)

seconds=soup.find('ul',class_='statistics-list')
seconds=seconds.b.text
seconds= seconds.replace(' sec','')
seconds=float(seconds)
seconds=1/seconds
print(seconds)

Second= seconds
Min=Second*60
Hours=Min*60
Days=Hours*24


# fin du scraping

Goal= int(input("How many trees do you want?"))


t=treecount
t=int(t)

if Goal < t:
    print("Run again, and put a value higher than " +str(t))
    sys. exit()
    
g=Goal
result= (g-t)/Second

unit = input("In which time unit do you want the result?:")

if unit.lower() in ["Seconds","seconds","SECONDS","s","sec"]:
    print("You have to wait:" +str(result),"Seconds")

elif  unit.lower() in ["Min","min","Minutes","minutes","m"]:
    print("You have to wait:" +str(result/60),"Minutes")

elif   unit.lower() in ["Hours","hours","H","h"]:
    print("You have to wait:" +str(result/3600),"Hours" )

elif unit.lower() in ["Days","days","D","d"]:
    print("You have to wait:" +str(result/86400),"Days")
    
elif unit.lower() in ["months","Months"]:
    print("You have to wait:" +str(result/2628000),"Months")

elif unit.lower() in ["years","Years","y"]:
    print("You have to wait:" +str(result/31536000),"Years")
    
    


workbook = xlsxwriter.Workbook('datas.xlsx') 

# By default worksheet names in the spreadsheet will be 
# Sheet1, Sheet2 etc., but we can also specify a name. 
worksheet = workbook.add_worksheet("Ecosia") 

# Some data we want to write to the worksheet. 
scores = ( 
	['Trees', 'Seconds'], 
	[t, Second], 
	
) 

# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 0
col = 0

# Iterate over the data and write it out row by row. 
for name, score in (scores): 
	worksheet.write(row, col, name) 
	worksheet.write(row, col + 1, score) 
	row += 1
    
print(scores)

workbook.close() 

    



