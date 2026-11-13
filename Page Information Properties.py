from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


## Title
'''
driver.get("https://www.decathlon.in/")
sleep(2)
title = driver.title
print("Title of page : ",title)'''

## url
'''
driver.get("https://www.decathlon.in/")
before = driver.current_url
print("Before url : ",before)
print("clicking on some link in the page")
sleep(8)
url = driver.current_url
print("URL of page : ",url)'''


## page source
'''
driver.get("https://www.decathlon.in/")
pg_src = driver.page_source
print("Page src : ",pg_src)'''


## TASK

#1) Open any webpage
#2) Fetch its title and url
'''
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(1)
title = driver.title
url = driver.current_url
print("Title of page : ",title)
print("URL of page : ",url)

'''


## TASK

#1) Open Amazon
#2) Fetch title and url
#3) Open Flipkart
#4) Fetch title and url
#5) Go back
#6) Fetch title and url
'''
print("Opening Amazon...")
driver.get('https://www.amazon.in/')
sleep(3)
print("Title : ", driver.title)
print("URL : ",driver.current_url)
sleep(2)
print("Opening Flipkart...")
driver.get('https://www.flipkart.com/')
sleep(2)
print("Title : ", driver.title)
print("URL : ",driver.current_url)
sleep(5)
print("Clicking the back button...")
driver.back()
sleep(2)
print("Title : ", driver.title)
print("URL : ",driver.current_url)
'''



##1) Open Crocs
##2) Fetch title and url
##3) Choose a product manually by giving sleep
##4) Fetch the title and url
'''
driver.get('https://www.crocs.in/')
sleep(2)
print("Title : ", driver.title)
print("URL : ",driver.current_url)

print("Clicking on a link....")
sleep(8)


if ("Brooklyn Sandals" in driver.title) and ("brooklyn-sandals" in driver.current_url):
    print("Successful navigation")
else:
    print("Failed")

'''



























