from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## close
'''
driver.get('https://www.crocs.in/')
sleep(5)  ##manually open some tabs
driver.close()
'''


## quit
'''
driver.get('https://www.crocs.in/')
sleep(5)
driver.quit()
'''



# TASK

#1) Open amazon
#2) Refresh
#3) Fetch title
#4) Open myntra
#5) Fetch title
#6) Close

print("Opening Amazon")
driver.get('https://www.amazon.in/')
sleep(2)
driver.refresh()
sleep(2)
print(driver.title)
print("Opening Myntra")
driver.get('https://www.myntra.com/')
sleep(2)
print(driver.title)
sleep(2)
driver.close()
