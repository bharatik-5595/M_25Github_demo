#1) Open youtube
#2) Search for anything and click search icon
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/webtables')
# driver.maximize_window()
# sleep(2)
# # Salary
# sal = driver.find_element(By.XPATH, '//td[text()="Cantrell"]/following-sibling::td[3]')
# print("Salary : ", sal.text)
# # First Name (the very first preceding sibling)
# fname = driver.find_element(By.XPATH, '//td[text()="Cantrell"]/preceding-sibling::td[1]')
# print("First Name : ", fname.text)
# driver.quit()

## TASK

#1) Open https://demowebshop.tricentis.com/
#2) Click on Apparel and Shoes
#3) Choose Low to High ---> Sort By dropdown
 #  Choose 4           ---> Display dropdown
 #  Choose List        ---> View As dropdown

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
# driver.get("https://demowebshop.tricentis.com/")
#
# # Click Apparel & Shoes
# wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//a[contains(text(),'Apparel & Shoes')]")
#     )
# ).click()
#
# # Sort By -> Low to High
# Select(
#     wait.until(
#         EC.presence_of_element_located(
#             (By.ID, "products-orderby")
#         )
#     )
# ).select_by_visible_text("Price: Low to High")
#
# # Display -> 4
# Select(
#     wait.until(
#         EC.presence_of_element_located(
#             (By.ID, "products-pagesize")
#         )
#     )
# ).select_by_visible_text("4")
#
# # View As -> List
# Select(
#     wait.until(
#         EC.presence_of_element_located(
#             (By.ID, "products-viewmode")
#         )
#     )
# ).select_by_visible_text("List")
#
# print("Task completed successfully!")
#
# # Keep browser open
# input("Press Enter to close browser...")
# driver.quit()
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.XPATH,'//input[@class="desktop-searchBar"]').click()
# driver.find_element(By.XPATH,'//input[@class="desktop-searchBar"]').send_keys("Shoes")
# sleep(3)
# search=driver.find_element(By.XPATH,'//input[@class="desktop-searchBar"]')
# search.send_keys("Shoes")
# sleep(2)






# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# sleep(2)
# ele = driver.find_element(By.XPATH, '//input[@placeholder="Search for products, brands and more"]').send_keys('Hoodies')
# sleep(3)
# sugg=driver.find_elements(By.XPATH,'//li[@class="desktop-suggestion null" and contains (text(),"Hoodies For Women")]')
# for i in sugg:
#     print(i.text)
#     i.click()
#     break





