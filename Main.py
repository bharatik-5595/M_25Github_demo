# from selenium.webdriver import Chrome
# driver = Chrome()
# from selenium.webdriver import Edge
# driver = Edge()
# from selenium.webdriver import Firefox
# driver = Firefox()
# from selenium.webdriver import Chrome,ChromeOptions
# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.amazon.in")
# from selenium.webdriver import Chrome,ChromeOptions
# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# from selenium.webdriver import Edge, EdgeOptions
# o = EdgeOptions()
# o.add_experimental_option("detach", True)
# driver = Edge(options=o)
# # Open Amazon in first tab
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# # Open Flipkart in new tab
# driver.execute_script("window.open('https://www.flipkart.com', '_blank');")
# # Switch to Flipkart tab (index 1)
# driver.switch_to.window(driver.window_handles[1])
# driver.minimize_window()
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.amazon.com")
# sleep(2)
# size= driver.get_window_size()
# print("Width:", size["width"])
# print("Height:", size["height"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.amazon.com")
# sleep(2)
# driver.set_window_size(1200, 800)
# size = driver.get_window_size()
# print("Width:", size["width"])
# print("Height:", size["height"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.flipkart.com")
# sleep(2)
# position= driver.get_window_position()
# print("X position:", position["x"])
# print("Y position:", position["y"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.flipkart.com")
# sleep(2)
# driver.set_window_position(100, 200)
# position = driver.get_window_position()
# print("X position:", position["x"])
# print("Y position:", position["y"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.flipkart.com")
# sleep(2)
# rect= driver.get_window_rect()
# print("X position:", rect["x"])
# print("Y position:", rect["y"])
# print("Width:", rect["width"])
# print("Height:", rect["height"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.flipkart.com")
# sleep(2)
# driver.set_window_rect(100,150,1200,800)
# rect = driver.get_window_rect()
# print("X position:", rect["x"])
# print("Y position:", rect["y"])
# print("Width:", rect["width"])
# print("Height:", rect["height"])
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.get("https://www.flipkart.com")
# sleep(5) ## click on a link manually
# driver.back()
# print("Current URL:", driver.current_url)
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.get("https://www.flipkart.com")
# sleep(5) ## click on a link manually
# driver.back()
# sleep(2)
# driver.forward()
# print("Current URL:", driver.current_url)
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# print("Title before refresh:", driver.title)
# driver.refresh()
# sleep(2)
# print("Title after refresh:", driver.title)
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# # Step 1: Open a website
# driver.get("https://www.google.com")
# driver.maximize_window()
# sleep(2)
# # Step 2: Get and print current window size
# size = driver.get_window_size()
# print("Width:", size["width"])
# print("Height:", size["height"])
# # Step 3: Get and print current window position
# position = driver.get_window_position()
# print("X position:", position["x"])
# print("Y position:", position["y"])
# # Step 4: Get and print current window rect
# rect = driver.get_window_rect()
# print("Rect:", rect)
# # Step 5: Change window size and position
# driver.set_window_size(1200, 800)
# driver.set_window_position(100, 150)
# # Step 6: Print updated rect
# updated_rect = driver.get_window_rect()
# print("Updated Rect:", updated_rect)
# # Step 7: Navigate to another website
# driver.get("https://www.flipkart.com")
# sleep(3)
# # Step 8: Go back to previous page
# driver.back()
# sleep(2)
# print("After back, URL:", driver.current_url)
# # Step 9: Go forward again
# driver.forward()
# sleep(2)
# print("After forward, URL:", driver.current_url)
# # Step 10: Refresh the page
# driver.refresh()
# sleep(2)
# print("After refresh, URL:", driver.current_url)
# from selenium.webdriver import Chrome, ChromeOptions
# from time import sleep
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# original_window = driver.current_window_handle
# driver.switch_to.new_window('tab')
# sleep(2)
# driver.close()
# driver.switch_to.window(original_window)
# print(driver.title)
# from selenium.webdriver import Chrome, ChromeOptions
# from time import sleep
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# original_window = driver.current_window_handle
# driver.switch_to.new_window('tab')
# sleep(2)
# driver.switch_to.window(original_window)
# print(driver.current_window_handle)
# driver.quit()
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.flipkart.com")
# sleep(2)
# title = driver.title
# print("Title:", title)
# url = driver.current_url
# print("URL:", url)
# print("Google in title:", "google" in title.lower())
# print("Google in URL:", "google" in url.lower())
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.google.com")
# sleep(2)
# source = driver.page_source
# length = len(source)
# print("Page source length:", length)
# print("Google in source:", "google" in source.lower())
# text = "Google"
# if text.lower() in source.lower():
#     print("Text found")
# else:
#     print("Text not found")
# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# # Open Google
# driver.get("https://www.google.com")
# sleep(2)
# # Store Google window handle
# current_handle = driver.current_window_handle
# print("Google handle:", current_handle)
# # Open new tab
# driver.switch_to.new_window("tab")
# # Open Python
# driver.get("https://www.python.org")
# sleep(2)
# # Store Python window handle
# python_handle = driver.current_window_handle
# print("Python handle:", python_handle)
# # Get all window handles
# handles = driver.window_handles
# print("All handles:", handles)
# # Switch back to Google
# driver.switch_to.window(current_handle)
# print("Google title:", driver.title)
# # Switch to Python
# driver.switch_to.window(python_handle)
# print("Python title:", driver.title)
# # Final information
# print("Current handle:", driver.current_window_handle)
# print("All handles:", driver.window_handles)
# print("Current title:", driver.title)

