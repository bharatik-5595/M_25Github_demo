from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## to maximize
'''driver.maximize_window()
sleep(6)'''


'''
## to minimize
driver.minimize_window()
sleep(4)

## to fullscreen
driver.fullscreen_window()'''


## To open a webpage
'''
driver.get('https://flipkart.com')
'''




## TASK

'''
1) 
--> Open Chrome browser
--> Open a webpage u like

2) 
--> Open Chrome browser
--> Use ChromeOptions to do browser setting
--> Open a webpage u like

3)
--> Open Chrome browser
--> Use ChromeOptions to do browser setting
--> Open a webpage u like
--> Maximize 

4) 
--> Open Edge browser
--> Use EdgeOptions to do browser setting
--> Open a webpage u like
--> Maximize 
--> Open another webpage
--> Minimize
'''


## get window size
'''
driver.get('https://www.nike.in/')
size_before = driver.get_window_size()
print("Before : ",size_before)
sleep(2)
driver.maximize_window()
sleep(2)
size_after = driver.get_window_size()
print("After : ",size_after)
'''


##  get window position
'''
driver.get('https://www.amazon.in')
sleep(2)
position_before = driver.get_window_position()
print("Before : ",position_before)
sleep(2)
driver.maximize_window()
sleep(2)
position_after = driver.get_window_position()
print("After : ",position_after)
driver.fullscreen_window()
sleep(2)
position_after_fs = driver.get_window_position()
print("After : ",position_after_fs)'''






## get window rect
'''
driver.get('https://www.amazon.in')
sleep(2)
rect_before = driver.get_window_rect()
print("Before : ",rect_before)
sleep(2)
driver.maximize_window()
sleep(2)
rect_after = driver.get_window_rect()
print("After : ",rect_after)
'''


## TASK

#1) Open any webpage u like
#2) Fetch its size,position and rect
#3) Maximize
#4) Fetch its size,position and rect




## set window size
'''
driver.get('https://www.amazon.in')
sleep(2)
driver.set_window_size(1800, 800)
'''

## set window position
'''
driver.get('https://www.amazon.in')
sleep(2)
driver.set_window_position(50,50)
'''

## set_window rect
'''
driver.get('https://www.amazon.in')
sleep(2)
driver.set_window_rect(50,50,800,600)
'''




## TASK

#1) Open a webpage u like
#2) Maximize
#3) Get the size and position
#4) Change the position to 70,70
#5) Change the size to 600,600

'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
rect_before = driver.get_window_rect()
print("Before : ",rect_before)
driver.set_window_position(70,70)
driver.set_window_size(600,600)

'''















