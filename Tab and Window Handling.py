# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
##current window handle
'''
driver.get("https://www.google.com")
sleep(2)
id_tab = driver.current_window_handle
print(id_tab)
'''

# FD093025F0C998339119D7041CC960D0
# C8B2380A38CD6C396A8784078755AEDC

'''
driver.get("https://www.google.com")
sleep(2)
id_tab = driver.current_window_handle
print(id_tab)
driver.get("https://www.flipkart.in")
sleep(2)
id_tab2 = driver.current_window_handle
print(id_tab2)
'''

## window handles
'''
driver.get("https://www.google.com")
sleep(5)                               ## manually open tabs
id_tab = driver.current_window_handle
handles = driver.window_handles
print(id_tab)
print(handles)

'''


## open a new tab
'''
driver.get("https://www.google.com")
sleep(5)
driver.switch_to.new_window('tab')
driver.get('https://www.amazon.in')

'''
## open a new window
'''
driver.get("https://www.google.com")
sleep(5)
driver.switch_to.new_window('window')
driver.get('https://www.amazon.in')
'''


'''
driver.get("https://www.google.com")
sleep(5)
driver.switch_to.new_window('tab')
driver.get('https://www.amazon.in')
sleep(3)
driver.close()
'''





'''
driver.get("https://www.google.com")
sleep(1)
print(driver.current_window_handle)
print(driver.title)
sleep(5)
driver.switch_to.new_window('tab')   ##plz open new tab
driver.get('https://www.amazon.in')
sleep(2)
print(driver.current_window_handle)
print(driver.title)
'''

## switch to window
'''
driver.get("https://www.myntra.com/mirrors")
sleep(1)
print(driver.current_window_handle)
print(driver.title)
sleep(8)     ## i will click a product

driver.switch_to.window(driver.window_handles[1])

print(driver.current_window_handle)
print(driver.title)
print(driver.window_handles)
'''
# ## TASK
# #1) Open Flipkart
# #2) Open Amazon in new tab
# #3) Open Myntra in new window
# ## Fetch all the window id's , title and url
# ## Fetch window handles
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# # 1. Open Flipkart
# driver.get("https://www.flipkart.com")
# sleep(2)
# # 2. Open Amazon in new tab
# driver.switch_to.new_window("tab")
# driver.get("https://www.amazon.com")
# sleep(2)
# # 3. Open Myntra in new window
# driver.switch_to.new_window("window")
# driver.get("https://www.myntra.com")
# sleep(2)
# # Fetch all window handles
# handles = driver.window_handles
# print("All handles:", handles)
# print("Total windows/tabs:", len(handles))
# # Fetch ID, title and URL of every window
# for handle in handles:
#     driver.switch_to.window(handle)
#     print("----------------------")
#     print("Window ID:", driver.current_window_handle)
#     print("Title:", driver.title)
#     print("URL:", driver.current_url)


