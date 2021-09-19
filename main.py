#first you need to download a chrome driver and set the location in to C:\Program Files (x86)
#be sure that your main google chrome and the driver is on the same version

from time import sleep
from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver1 = webdriver.Chrome(PATH)
driver2 = webdriver.Chrome(PATH)
driver3 = webdriver.Chrome(PATH)
driver4 = webdriver.Chrome(PATH)
driver5 = webdriver.Chrome(PATH)

driver1.get('https://youtu.be/oB-3IPdAbnM')
driver2.get('https://youtu.be/oB-3IPdAbnM')
driver3.get('https://youtu.be/oB-3IPdAbnM')
driver4.get('https://youtu.be/oB-3IPdAbnM')
driver5.get('https://youtu.be/oB-3IPdAbnM')
while True:
    sleep(40) #it will refresh chrome every 40 seconds, don't set this lower than 30
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
    driver5.refresh()
