#1) Write a program to count how many vowels are present in
#   text = "Automation Testing"
'''
text = input('Enter a string : ')
count = 0

for ch in text:
    if ch.lower() in 'aeiou':
        count += 1

print("No: of vowels : ",count)'''

#2) Write a program that accepts username and password
#Print :
# Login successful if both are correct
# Invalid username if username is wrong
# Invalid password if password is wrong

'''
un = input('Enter username : ')
pwd = input('Enter password : ')

if un != "admin":
    print("Invalid username")
elif pwd != "123456":
    print("Invalid password")
else:
    print("Logged in")'''


#3) Create a func is_even() that accepts a number and return True if
# is even , otherwise False
'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input('Enter a number : '))

print(is_even(n))
'''

# pip install selenium
# py -m pip install selenium
# python -m pip install selenium

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.decathlon.in/")
driver.maximize_window()

sleep(3)
driver.find_element(By.XPATH, '//a[@href="/shop/Bags-Store"]').click()

sleep(3)
driver.find_element(By.XPATH, '//a[@href="/c/little-explorers-930014"]').click()

sleep(3)
driver.find_element(By.XPATH, '(//div[@data-test-id="product-card:container"])[1]').click()

sleep(3)
driver.find_element(By.XPATH, '//button[@data-test-id="add-to-cart-button"]').click()

sleep(2)
driver.quit()
