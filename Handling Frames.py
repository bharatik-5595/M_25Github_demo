# from selenium.webdriver import Chrome, ChromeOptions, ActionChains
# from time import sleep
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)

## without switching
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
sleep(2)
ele = driver.find_element(By.ID,'inp2')
action = ActionChains(driver)
action.send_keys_to_element(ele,"Second inp")
sleep(2)
driver.find_element(By.ID,'inp3').send_keys('Third inp')'''


## index as argument
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp2').send_keys("Second inp")
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp3').send_keys('Third inp')
'''

'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
driver.switch_to.frame(0)
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp3').send_keys('Third inp')

'''


## name as argument


'''driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
driver.switch_to.frame('frame1')
driver.find_element(By.ID,'inp2').send_keys("Second inp")
driver.switch_to.frame('frame2')
driver.find_element(By.ID,'inp3').send_keys('Third inp')'''



## web element as argument


driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
frame1  = driver.find_element(By.XPATH,'//iframe[@src="page2.html"]')
driver.switch_to.frame(frame1)
driver.find_element(By.ID,'inp2').send_keys("Second inp")
frame2 = driver.find_element(By.XPATH,'//iframe[@src="page3.html"]')
driver.switch_to.frame(frame2)
driver.find_element(By.ID,'inp3').send_keys('Third inp')


## parent frame
'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
driver.find_element(By.ID,'inp1').send_keys('First inp')
driver.switch_to.frame('frame1')
driver.find_element(By.ID,'inp2').send_keys("Second inp")
driver.switch_to.frame('frame2')
driver.find_element(By.ID,'inp3').send_keys('Third inp')
driver.switch_to.parent_frame()
driver.find_element(By.ID,'inp2').clear()
driver.find_element(By.ID,'inp2').send_keys("back to inp2")

'''

## default content

# driver.get('file:///C:/Users/Qsp/Desktop/HTML/page1.html')
# driver.find_element(By.ID,'inp1').send_keys('First inp')
# driver.switch_to.frame('frame1')
# driver.find_element(By.ID,'inp2').send_keys("Second inp")
# driver.switch_to.frame('frame2')
# driver.find_element(By.ID,'inp3').send_keys('Third inp')
# driver.switch_to.default_content()
# driver.find_element(By.ID,'inp1').clear()
# driver.find_element(By.ID,'inp1').send_keys('back to First inp')





