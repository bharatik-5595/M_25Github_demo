from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")
# prefs = {"profile.default_content_settings.notifications": 2 ,"safebrowsing.enabled":True}
o.add_experimental_option("prefs", { "profile.default_content_settings.notifications": 2 })

driver = Chrome(options=o)

driver.execute_cdp_cmd(
    "Browser.setPermission",{
        "permission":{"name":"geolocation"},
        "setting":"denied",
        "origin":"https://www.easemytrip.com/"
    }
)


## Simple alert
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'alertBtn').click()
sleep(2)
alert = driver.switch_to.alert
sleep(2)
alert.accept()'''



## Confirmation
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'confirmBtn').click()
sleep(2)
alert = driver.switch_to.alert
# alert.accept()   # to click OK
alert.dismiss()'''



## Prompt

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'promptBtn').click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys("abc")
alert.accept()   # to click OK
# alert.dismiss()
'''





##Single File upload
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'singleFileInput').send_keys("C://Users//Qsp//PycharmProjects//M25_10am_12pm//Part_B//Javascript Execute Scripts.py")
sleep(1)
driver.find_element(By.XPATH,'//button[text()="Upload Single File"]').click()

'''


## Multiple File upload

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'multipleFilesInput').send_keys("C://Users//Qsp//PycharmProjects//M25_10am_12pm//Part_B//Javascript Execute Scripts.py\n","C://Users//Qsp//PycharmProjects//M25_10am_12pm//Part_B//Synchronization.py")
sleep(1)
driver.find_element(By.XPATH,'//button[text()="Upload Single File"]').click()

'''



## TASK
#1) Open https://omayo.blogspot.com/
#2) Upload file
#3) Handle Simple,Prompt, Confirmation Alert



## File download
# Unverified download blocked --> Turn on safe browsing
'''
driver.get('https://www.python.org/downloads/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[text()="Python 3.15.0"])[4]').click()
'''

'''
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
driver = Chrome(options=o)


driver.get('https://www.python.org/downloads/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[text()="Python 3.15.0"])[4]').click()
'''


## Regular HTML popups
'''
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="✕"]').click()
'''




driver.get('https://www.easemytrip.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,'ddate').click()
driver.find_element(By.XPATH,'//img[@id="img2Nex"]').click()
sleep(2)
driver.find_element(By.XPATH,'//img[@id="img2Nex"]').click()
sleep(2)
driver.find_element(By.ID,'trd_5_15/01/2027').click()














