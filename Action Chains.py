from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## click

'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//a[text()="Mobiles"]')
action = ActionChains(driver)
action.click(ele).perform()
'''


## mouse hover
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//span[@id = "nav-link-accountList-nav-line-1"]')
action = ActionChains(driver)
# action.move_to_element(ele).perform()
action.click(ele).perform()'''



## TASK
#1) Open https://www.nike.in/
#2) Hover on Kids
#3) Sleep of 5 sec and click on it



## double click
'''
driver.get('https://demoqa.com/buttons')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'doubleClickBtn')
action = ActionChains(driver)
action.double_click(ele).perform()

'''


## right click
'''
driver.get('https://demoqa.com/buttons')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'rightClickBtn')
action = ActionChains(driver)
action.context_click(ele).perform()
'''



## TASK

#1) Open https://testautomationpractice.blogspot.com/
#2) Click on START button
#3) Mouse hover on  POINT ME
#4) Double click on COPY TEXT


## click and hold
'''
driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'password').send_keys('myPassword')
sleep(2)
ele = driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action = ActionChains(driver)
action.click_and_hold(ele).perform()
'''



## release

'''
driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'password').send_keys('myPassword')
sleep(2)
ele = driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action = ActionChains(driver)
action.click_and_hold(ele).release().perform()

'''

## pause
'''
driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'password').send_keys('myPassword')
sleep(2)
ele = driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action = ActionChains(driver)
action.click_and_hold(ele).pause(5).release().perform()

'''


# drag and drop

'''driver.get('https://www.selenium.dev/selenium/web/mouse_interaction')
driver.maximize_window()
sleep(2)
drag_ele = driver.find_element(By.ID,'draggable')
drop_ele = driver.find_element(By.ID,'droppable')
actions = ActionChains(driver)
actions.pause(2).drag_and_drop(drag_ele,drop_ele).perform()'''


## drag and drop by offset
'''
driver.get('https://www.selenium.dev/selenium/web/mouse_interaction')
driver.maximize_window()
sleep(2)
drag_ele = driver.find_element(By.ID,'draggable')
actions = ActionChains(driver)
actions.pause(2).drag_and_drop_by_offset(drag_ele,60,60).perform()
'''


'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
drag = driver.find_element(By.ID,'draggable')
drop = driver.find_element(By.ID,'droppable')
actions = ActionChains(driver)
actions.drag_and_drop(drag,drop).perform()

'''

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
drag = driver.find_element(By.ID,'draggable')
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(drag,100,50).perform()

'''


# scroll to element
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
action = ActionChains(driver)
action.scroll_to_element(ele).perform()

'''


## scroll by amount
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
action = ActionChains(driver)
action.scroll_by_amount(0,200).perform()
sleep(2)
action.scroll_by_amount(0,200).perform()
'''


## scroll from origin
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
action = ActionChains(driver)
origin = ScrollOrigin.from_element(ele)
action.scroll_from_origin(origin,0,300).perform()'''



## send_keys_to_element
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'name')
action = ActionChains(driver)
action.send_keys_to_element(ele,"Doremon").perform()

'''



## TASK

#1) Open YouTube
#2) Search for anything and click search icon
#3) Scroll 500px
#4) Scroll to a particular element
#5) Scroll 200px from the element









