# # from selenium.webdriver import Chrome,ChromeOptions
# # from time import sleep
# #
# # from selenium.webdriver.common.by import By    ## import
# #
# # o = ChromeOptions()
# # o.add_experimental_option("detach", True)
# # driver = Chrome(options=o)
#
# '''
# ## click()
#
# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,'//a[text()="Mobiles"]').click()
#
#
# ##send_keys()
# sleep(2)
# ele = driver.find_element(By.ID,'twotabsearchtextbox')
# ele.send_keys('iphone 18 pro')
#
#
# ## clear()
# sleep(2)
# ele.clear()'''
#
#
# #TASK
#
# #1) Open Youtube
# #2) search for something
# #3) click on search icon
# #4) clear the search
# #5) search for something else and click
#
# '''
# driver.get('https://www.youtube.com/')
# driver.maximize_window()
# sleep(2)
# search_inp = driver.find_element(By.XPATH,'//input[@name="search_query"]')
# search_inp.send_keys('Mr Bean')
# search_btn = driver.find_element(By.XPATH,'//button[@aria-label="Search"]')
# search_btn.click()
# sleep(2)
# search_inp.clear()
# search_inp.send_keys('Tom and Jerry')
# sleep(2)
# search_btn.click()'''
#
#
#
#
#
#
#
# ## is displayed
# '''
# driver.get('https://www.facebook.com/')
# driver.maximize_window()
# sleep(2)
# email_ele = driver.find_element(By.XPATH,'//input[@name="email"]')
# print("Email displayed : ",email_ele.is_displayed())
#
# hidden_div = driver.find_element(By.XPATH,'//input[@type="submit"]/..')
# print("Hidden div displayed : ",hidden_div.is_displayed())
# '''
#
#
#
#
# ## is enabled
# '''
# driver.get('https://www.naukri.com/registration/createAccount?othersrcp=22636')
# driver.maximize_window()
# sleep(2)
# btn = driver.find_element(By.XPATH,'//button[@type="submit"]')
# print("Button displayed : ",btn.is_displayed())
# print("Button enabled : ",btn.is_enabled())'''
#
#
#
# ## is selected
# '''
# driver.get('https://demoqa.com/radio-button')
# driver.maximize_window()
# sleep(2)
# yes = driver.find_element(By.ID,'yesRadio')
# print("Yes displayed : ",yes.is_displayed())
# print("Yes enabled : ",yes.is_enabled())
# print("Yes selected : ",yes.is_selected())
# sleep(2)
# yes.click()
# sleep(2)
# print("After clicking ....")
# print("Yes selected : ",yes.is_selected())'''
#
#
#
# ## TASK
# #1) Open https://demowebshop.tricentis.com/register
# #2) Locate gender
# #3) Check if it is displayed, is enabled and is selected
# #4) click on it
# #5) Check if its selected after clicking
#
#
# yes = driver.find_element(By.ID,'yesRadio')
# print(yes.tag_name)'''
#
# ## get attribute
# '''
# driver.get('https://demoqa.com/radio-button')
# driver.maximize_window()
# sleep(2)
#
# yes = driver.find_element(By.ID,'yesRadio')
# print(yes.get_attribute('class'))
# print(yes.get_attribute('type'))
# print(yes.get_attribute('name'))'''
#
#
# ## text
# # '''driver.get('https://demoqa.com/radio-button')
# # driver.maximize_window()
# # sleep(2)
# # ele = driver.find_element(By.XPATH,'//label[@for="yesRadio"]')
# # print(ele.text)'''
#
#
#
# ## TASk
#
# #1) Open https://demowebshop.tricentis.com/register
# #2) Locate = Register link , Register button
# #3) Find their tag name
# #4) Find any 2 attribute values for each
# #5) Find the visible text of the elements
#
#
#
#
# ## size and location
# '''
# driver.get('https://demoqa.com/radio-button')
# driver.maximize_window()
# sleep(2)
# ele = driver.find_element(By.XPATH,'//label[@for="yesRadio"]')
# print(ele.size)
# print(ele.location)
# print(ele.rect)
#
# '''
#
#
#
# ## TASK
#
# #1) Open Amazon
# #2) Fetch size,position and rect of search field and search button
# #3) Fetch its 2 attribute values
# #4) Check if its displayed and enabled
# #5) Pass and input and click on the button
#
#
#
#
#
# ## TASK
#
# #1) Open Flipkart
# #2) Sleep - close the popup manually
# #3) Search for mobiles
# #4) Using mobile name , fetch the price
#
#
#
#
# driver.get('https://www.flipkart.com/')
# driver.maximize_window()
# sleep(5)
# driver.find_element(By.XPATH,'//input[@placeholder="Search for Products, Brands and More"]').send_keys('mobiles')
# sleep(2)
# driver.find_element(By.XPATH,'//button[@aria-label="Search for Products, Brands and More"]').click()
# sleep(3)
# ele = driver.find_element(By.XPATH,'//div[text()="Samsung Galaxy F07 (Green, 64 GB)"]/../following-sibling::div//div[@class="hZ3P6w DeU9vF"]')
# print(ele.text)
#
#
#
#
#
