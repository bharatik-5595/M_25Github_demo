from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## scroll By
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollBy(0,400)")
sleep(3)
driver.execute_script("window.scrollBy(0,500)")
'''


## scrollTo
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0,400)")
sleep(3)
driver.execute_script("window.scrollTo(0,500)")
'''


'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0,400)")
sleep(3)
driver.execute_script("window.scrollTo(0,0)")

'''


## Scroll to bottom

'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

'''



## scroll to element

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//h2[text()="Mouse Hover"]')
driver.execute_script("arguments[0].scrollIntoView(true)",ele)
'''


## click

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//button[text()="New Tab"]')
driver.execute_script("arguments[0].click()",ele)

'''

## send keys

'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'name')
driver.execute_script("arguments[0].value = 'Amrutha' ",ele)


'''


# 1) Open Amazon
# 2) Search for a product
# 3) Click on search icon
# 4) Scroll by 500px


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # 1. Open Amazon India
    driver.get("https://www.amazon.in/")

    # 2. Search for a product
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("wireless headphones")

    # 3. Click the search icon
    wait.until(
        EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
    ).click()

    # Wait for search results to load
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        )
    )

    # 4. Scroll down by 500 pixels using JavaScript
    driver.execute_script("window.scrollBy(0, 500);")

finally:
    driver.quit()






















































