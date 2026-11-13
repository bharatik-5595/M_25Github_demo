from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## back
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(10) ## click on a link manually
driver.back()

## forward

sleep(5)
driver.forward()

## reload
sleep(3)
driver.refresh()
'''



## TASK

#1) Open wikipedia
#2) Maximize
#3) Refresh
#4) Open w3school
#5) Refresh
#6) Go back


driver.get('https://www.wikipedia.org/')
driver.maximize_window()
driver.refresh()
sleep(2)
driver.get('https://www.w3schools.com/')
driver.refresh()
sleep(2)
driver.back()
















