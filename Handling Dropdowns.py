# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By    ## import
# from selenium.webdriver.support.ui import Select
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)

## select by visible text
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_visible_text('Tamil Nadu')'''
from selenium.webdriver.common import keys

## select by index
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_index(3)

'''


## select by value
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_value('MH')
sleep(1)
option.select_by_index(3)
sleep(1)
option.select_by_visible_text('Tamil Nadu')'''




## multi select

'''driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown2 = driver.find_element(By.ID,'hobbies')
option = Select(dropdown2)
option.select_by_index(0)
sleep(1)
option.select_by_visible_text('Cooking')
sleep(1)
option.select_by_value('garden')'''



## deselect
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown2 = driver.find_element(By.ID,'hobbies')
option = Select(dropdown2)
option.select_by_index(0)
sleep(1)
option.select_by_index(1)
sleep(1)
option.select_by_visible_text('Cooking')
sleep(1)
option.select_by_value('garden')

# sleep(2)
# option.deselect_by_index(1)
# sleep(1)
# option.deselect_by_visible_text('Gardening')
# sleep(1)
# option.deselect_by_value('cook')

option.deselect_all()'''







## TASK

#1) Open https://demowebshop.tricentis.com/
#2) Click on Apparel and Shoes
#3) Choose Low to High ---> Sort By dropdown
 #  Choose 4           ---> Display dropdown
 #  Choose List        ---> View As dropdown


## TASK

#1) Open https://www.bmrc.co.in/
#2) Click English
#3) Choose From station
#4) Choose To station
#5) Click Get Details









# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
#
# from selenium.webdriver.common.by import By    ## import
# from selenium.webdriver.support.ui import Select
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)

## select by visible text
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_visible_text('Tamil Nadu')'''


## select by index
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_index(3)

'''


## select by value
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1 = driver.find_element(By.ID,'loc')
option = Select(dropdown1)
option.select_by_value('MH')
sleep(1)
option.select_by_index(3)
sleep(1)
option.select_by_visible_text('Tamil Nadu')'''




## multi select

'''driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown2 = driver.find_element(By.ID,'hobbies')
option = Select(dropdown2)
option.select_by_index(0)
sleep(1)
option.select_by_visible_text('Cooking')
sleep(1)
option.select_by_value('garden')'''



## deselect
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown2 = driver.find_element(By.ID,'hobbies')
option = Select(dropdown2)
option.select_by_index(0)
sleep(1)
option.select_by_index(1)
sleep(1)
option.select_by_visible_text('Cooking')
sleep(1)
option.select_by_value('garden')

# sleep(2)
# option.deselect_by_index(1)
# sleep(1)
# option.deselect_by_visible_text('Gardening')
# sleep(1)
# option.deselect_by_value('cook')

option.deselect_all()'''







## TASK

#1) Open https://demowebshop.tricentis.com/
#2) Click on Apparel
# l and Shoes
#3) Choose Low to High ---> Sort By dropdown
 #  Choose 4           ---> Display dropdown
 #  Choose List        ---> View As dropdown





## TASK

#1) Open https://www.bmrc.co.in/
#2) Click English
#3) Choose From station
#4) Choose To station
#5) Click Get Details
'''
driver.get('https://www.bmrc.co.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//span[text()="English"]').click()
sleep(1)
from_station = driver.find_element(By.XPATH,'(//select[@class="form-control select fare-selects"])[1]')
option1 = Select(from_station)
option1.select_by_visible_text('Benngiganahalli')
to_station = driver.find_element(By.XPATH,'(//select[@class="form-control select fare-selects"])[2]')
option2 = Select(to_station)
option2.select_by_visible_text('Nagasandra')
sleep(1)
driver.find_element(By.XPATH,'(//button[@type="button"])[2]').click()
'''
## TASK
#1) Open https://www.bmrc.co.in/
#2) Click English
#3) Choose From station
#4) Choose To station
#5) Click Get Details
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.bmrc.co.in/")
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# # Click English link
# english_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="English"]')))
# english_btn.click()
# # Select From Station
# from_station = wait.until(EC.presence_of_element_located((By.XPATH, '(//select[@class="form-control select fare-selects"])[1]')))
# Select(from_station).select_by_visible_text("Baiyappanahalli")
# # Select To Station
# to_station = wait.until(EC.presence_of_element_located((By.XPATH, '(//select[@class="form-control select fare-selects"])[2]')))
# Select(to_station).select_by_visible_text("Nagasandra")
# # Click Submit
# submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[2]')))
# submit_btn.click()
# # Close popup
# close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Close")]')))
# close_btn.click()
# driver.quit()





## Auto suggestions
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('perfume')
sleep(2)
sugg = driver.find_elements(By.XPATH,'//div[@class="s-suggestion-container"]')
# print(sugg)

for i in sugg:               #[10,20,30]
    # print(i.text)
    if "perfume organizer" in i.text :
        i.click()
        break
'''


'''
driver.get('https://www.google.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//textarea[@name="q"]').send_keys('selenium automation')
sleep(2)
sugg = driver.find_elements(By.XPATH,'//li[@data-attrid="AutocompletePrediction"]')
for i in sugg:
    # print(i.text)
    if " interview questions and answers" in i.text:
        i.click()
        break
'''


















































