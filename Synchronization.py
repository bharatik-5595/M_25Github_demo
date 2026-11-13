# from selenium.webdriver import Chrome, ChromeOptions, ActionChains
# import time
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)



## static wait
'''
driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(10)
driver.find_element(By.XPATH,'//div[text()="Food & Health"]').click()
sleep(10)
ele = driver.find_element(By.XPATH,'//div[text()="Chocolates "]')
action = ActionChains(driver)
action.scroll_to_element(ele).click(ele).perform()'''
from selenium.common import NoSuchElementException

## implicit wait
'''
start_time = time.time()
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="✕"]').click()
driver.find_element(By.XPATH,'//div[text()="Food & Health"]').click()
ele = driver.find_element(By.XPATH,'//div[text()="Chocolates "]')
action = ActionChains(driver)
action.scroll_to_element(ele).click(ele).perform()
end_time = time.time()

exec_total_time = end_time - start_time
print(exec_total_time)
'''


## TASK - i) using sleep    ii) using implicit wait

#1) Open https://www.decathlon.in/
#2) Click on Bags and Backpacks
#3) Click on Little Explorers
#4) Choose any 1
#5) Add to Cart

'''
driver.get('https://www.decathlon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[@href="/shop/Bags-Store"]').click()
driver.find_element(By.XPATH,'//a[@href="/c/little-explorers-930014"]').click()
driver.find_element(By.XPATH,'(//div[@data-test-id="product-card:container"])[4]').click()
driver.find_element(By.XPATH,'//span[text()="Add to cart"]').click()
driver.quit()'''



#TASK

#1) Open https://www.nike.in/
#2) Click on Kids
#3) Choose footwear
#4) Choose a shoe
#5) Select Size and Add to Bag


'''
driver.get('https://www.nike.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="Kids"]').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,'//li[text()="Apparel"]').click()
driver.find_element(By.XPATH,'//a[@href="/nike-sportswear-older-kids-girls-short-sleeve-polo-top/p/27753592"]').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,'//label[text()="XS"]').click()
driver.find_element(By.XPATH,'//button[text()="Add to Bag"]').click()

'''



'''
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID,'start').click()
ele = driver.find_element(By.ID,'finish')
print(ele.text)
'''


## explicit wait


from selenium.webdriver import Edge, EdgeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

o = EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)



'''
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.maximize_window()

driver.find_element(By.XPATH,'//button[text()="Start"]').click()
wait = WebDriverWait(driver, 15)
text_ele = wait.until(EC.visibility_of_element_located((By.ID,'finish')))
print(text_ele.text)

'''



'''
driver.get('https://www.shoppersstack.com/')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//span[text()="ORAL B"]').click()
driver.find_element(By.ID,'Check Delivery').send_keys("560043")
driver.find_element(By.ID,'Check').click()
#
wait = WebDriverWait(driver, 15)
# check_btn = wait.until(EC.element_to_be_clickable((By.ID,'Check')))
# check_btn.click()
'''




'''
driver.get('https://www.shoppersstack.com/')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//span[text()="ORAL B"]').click()
driver.find_element(By.ID,'Check Delivery').send_keys("560043")

wait = WebDriverWait(driver, 15,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
check_btn = wait.until(EC.element_to_be_clickable((By.ID,'Check')))
check_btn.click()

'''





#TASK  ---> using explicit wait

#1) Open https://www.amazon.in/
#2) Search for a product
#3) Click on search icon
#4) Choose a product
#5) Add to cart

'''

driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 15)
searc_ele = wait.until(EC.visibility_of_element_located((By.ID,'twotabsearchtextbox')))
searc_ele.send_keys("perfume")
search_btn = wait.until(EC.element_to_be_clickable((By.ID,'nav-search-submit-button')))
search_btn.click()
item = wait.until(EC.visibility_of_element_located((By.XPATH,'(//span[@data-csa-c-type="item"])[1]')))
item.click()
driver.switch_to.window((driver.window_handles[-1]))
add_to_cart = wait.until(EC.visibility_of_element_located((By.ID,'add-to-cart-button')))
add_to_cart.click()'''




## TASK

#1) Open https://demowebshop.tricentis.com/register
#2) Fill all details
#3) Click Register



driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)

gender = wait.until(EC.element_to_be_clickable((By.ID,'gender-female')))
gender.click()
fname = wait.until(EC.visibility_of_element_located((By.ID,'FirstName')))
fname.send_keys("Julie")
lname = wait.until(EC.visibility_of_element_located((By.ID,'LastName')))
lname.send_keys('Jack')
email = wait.until(EC.visibility_of_element_located((By.ID,'Email')))
email.send_keys("juliejack@gmail.com")
pwd = wait.until(EC.visibility_of_element_located((By.ID,'Password')))
pwd.send_keys("juliekack@321")
cnf_pwd = wait.until(EC.visibility_of_element_located((By.ID,'ConfirmPassword')))
cnf_pwd.send_keys("juliekack@321")
register = wait.until(EC.element_to_be_clickable((By.ID,'register-button')))
register.click()












































