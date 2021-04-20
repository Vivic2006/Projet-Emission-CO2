#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:01:20 2021

@author: victorbuzy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
import urllib.request
def remove(miles): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', miles)
Path = '/Users/victorbuzy/Desktop/chromedriver'





options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional

Start=(input("What is your current location?"))
Arrive=(input("Where do you want to go?"))
Persons=(int(input(("How many personns are traveling with you?"))))
Gallons= float(1.5398) #Gallons pour faire 100KM pour voiture Mazda'
Conversion= float(62.1504) #Conversion de 100KM en Miles
CO2= float(10.36488) #Kg de co2 emis par Gallons
Tree=int(30) #1 tree catch 30KG of CO2/Year ECOTREE Source


driver = webdriver.Chrome(Path)
driver.get("https://www.google.com/maps")
time.sleep(3)
search = driver.find_element_by_css_selector('#searchboxinput')
search.send_keys(Start)
search.send_keys(Keys.RETURN)
time.sleep(3)
python_button = driver.find_element_by_css_selector('#searchbox-searchbutton').click()
time.sleep(5)


unit = driver.find_element_by_css_selector('#pane > div > div.widget-pane-content.scrollable-y > div > div > div.section-hero-header-title > div.section-hero-header-title-top-container > div.section-hero-header-title-description > h2 > span')
unit=unit.text
print(unit)
driver.close()
driver.quit()



states = ['AL', "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


if unit.lower() in ["Alabama","Al","AL","al","alabama"]:
    states='AL'
elif unit.lower() in ["Alaska","AK","Ak","ak","alaska"]:
    states='AK'
elif unit.lower() in ["Arizona","AZ","Az","az","arizona"]:
    states='AZ'
elif unit.lower() in ["Arkansas","AK","Ak","ak","arkansas"]:
    states='AR'
elif unit.lower() in ["Ca","Californie","CA","californie","ca"]:
    states='CA'
elif unit.lower() in ["CO","Calorado","co","calorado","Co"]:
    states='CO'   
elif unit.lower() in ["CT","Connecticut","ct","connecticut","Ct"]:
    states='CT' 
elif unit.lower() in ["DC","Disctrict of Columbia","dc","district of columbia","Dc"]:
    states='DC'
elif unit.lower() in ["DE","Delaware","de","delaware","De"]:
    states='DE' 
elif unit.lower() in ["FL","Floride","fl","floride","Fl"]:
    states='FL' 
elif unit.lower() in ["GA","Georgia","ga","georgia","Ga"]:
    states='GA'
elif unit.lower() in ["HI","Hawaii","hi","Hawaii","Ha"]:
    states='HI'
elif unit.lower() in ["ID","Idaho","id","idaho","Id"]:
    states='ID'
elif unit.lower() in ["IL","Illinois","il","illinois","Illinois"]:
    states='IL'

print(states)    
    
driver = webdriver.Chrome(Path)

driver.get("https://gasprices.aaa.com/?state="+str(states))
time.sleep(5)

Price = driver.find_element_by_css_selector ('body > main > div.container.mob-cont > table > tbody > tr:nth-child(1) > td:nth-child(2)')
Price=Price.text
Price = Price.replace('$','')
Price=float(Price)
print(Price)

driver.close()
driver.quit()




options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional



Path = '/Users/victorbuzy/Desktop/chromedriver'
driver = webdriver.Chrome(Path)

driver.get("https://www.google.fr/maps/@25.7533165,-80.1923844,14z")
time.sleep(5)

# click itineraire button
python_button = driver.find_element_by_css_selector('#searchbox-directions > img')

python_button.click()
time.sleep(2)

#Put the location in Google Maps
search = driver.find_element_by_css_selector('#sb_ifc51 > input')
search.send_keys(Start)
search.send_keys(Keys.RETURN)
time.sleep(3)

search2 = driver.find_element_by_css_selector('#sb_ifc52 > input')
search2.send_keys(Arrive)
search2.send_keys(Keys.RETURN)

time.sleep(6)

miles = driver.find_element_by_css_selector('#section-directions-trip-0 > div > div:nth-child(1) > div.section-directions-trip-numbers > div.section-directions-trip-distance.section-directions-trip-secondary-text > div')
miles = miles.text
driver.close()
driver.quit()
miles = miles.replace('miles','')
miles=miles.replace(' ','')
miles = miles.replace(',','.')
miles=remove(miles)

miles=float(miles)
print('You have to drive:' +str(miles), 'miles')

Conso = ((Gallons * miles)/ Conversion)
Conso =float(Conso)
print('Your consumation is:' +str(Conso), 'Gallons')

Cost = (Conso * Price)/Persons
Cost = float(Cost)
print('The price of this trip is:' +str(Cost), '$')

Emission = (CO2 * Conso)/Persons
Emission=float(Emission)
print('Your CO2 emission for this trip is:' +str(Emission), 'Kg in the atmosphere')

Nbtree= (Emission/Tree)
Nb= float(Nbtree)
print('For this trip you have to plant '+str(Nb),'or to do ' +str(Nb*45),'Searches on Ecosia to be CO2 neutral')


























