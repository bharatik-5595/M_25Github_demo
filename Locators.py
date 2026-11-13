from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By    ## import

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## ID
'''
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'Welcome_to_Wikipedia')
print("Welcome to wikipedia found!!")

'''

'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,"twotabsearchtextbox")  ## find element
ele.send_keys('shoe')
sleep(2)
btn = driver.find_element(By.ID,'nav-search-submit-button')
btn.click()
sleep(5)
driver.close()
'''


## NAME

'''driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
# ele = driver.find_element(By.NAME,"field-keywords")
# ele.send_keys('bottle')
driver.find_element(By.NAME,'field-keywords').send_keys('bottle')'''


## CLASS NAME
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,'nav-input.nav-progressive-attribute').send_keys('perfume')

'''

## TAG NAME
'''
driver.get('https://www.google.com')
driver.maximize_window()
sleep(2)
driver.find_element(By.TAG_NAME,'textarea').send_keys('python selenium')

'''
## TASK - 1
# 1) Using TAGNAME click on link in https://www.google.com
'''
driver.get('https://www.google.com')
driver.maximize_window()
sleep(2)
driver.find_element(By.TAG_NAME,'a').click()
'''
## TASK - 2

#1) Open https://demoqa.com/text-box
#2) i) Enter Fullname,email,current address, permanent address using ID locator
#  ii) Use classname and use tagname


## TASK - 3
#1) Open https://www.facebook.com/
#2) Enter email and password using - NAME


## TASK - 4
#1) Open https://www.youtube.com/
#2) Search for any video - NAME , CLASSNAME
#3) Click on Search button - CLASSNAME

##TASK - 5 (Any locator)
#1) Open https://demowebshop.tricentis.com/register
#2) Fill all details and click Submit


############################################################################################

##LINK TEXT
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
# driver.find_element(By.LINK_TEXT,'Mobiles').click()

'''

'''
driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(5)
driver.find_element(By.LINK_TEXT,'Login').click()
'''

## TASK
#1) Open https://www.crocs.in/
#2) Fetch url
#3) Click on a link - using link text locator
#4) Fetch url


'''
driver.get('https://www.crocs.in/')
driver.maximize_window()
sleep(2)
before = driver.current_url
print("Before clicking : ",before)
sleep(2)
driver.find_element(By.LINK_TEXT,'Bestsellers').click()
sleep(2)
after = driver.current_url
print("After clicking : ",after)
'''



## TASK
#1) Open https://www.lenskart.com/
#2) Click on a link
'''
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,'CONTACTS').click()

'''


## PARTIAL LINK TEXT
'''
driver.get('https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers')
driver.maximize_window()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,'Ghar Soaps Sandalwood & Saffron').click()
'''

###TASK
## 1) Open https://www.fortishealthcare.com/
## 2) click Find a doctor


###TASK
## 1) Open Amazon
## 2) Click on Electronics
## 3) Click Home theater, TV and Video

'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Electronics').click()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,'Home Theater').click()
'''


#######################################################################################################

##  CSS Selectors
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'a[href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics"]').click()
'''


'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys('perfume')
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()

'''

'''
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Full Name"]').send_keys('Dora')
driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys('dora.theexplorer@gmail.com')
driver.find_element(By.CSS_SELECTOR,'textarea[id="currentAddress"]').send_keys('Jungle\nForest')
driver.find_element(By.CSS_SELECTOR,'textarea[id="permanentAddress"]').send_keys('Jungle')
driver.find_element(By.CSS_SELECTOR,'button[type="button"][id="submit"]').click()
'''

'''
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'a[href="https://www.johnjacobseyewear.com/"]').click()

'''

'''
driver.get('https://www.instagram.com/')
driver.maximize_window()
sleep(5)
driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys('dora@1234')
driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('dora@1234abc')
driver.find_element(By.CSS_SELECTOR,'div[aria-label="Log In"][role="button"]').click()
'''


## TASK
#1) Open Youtube
#2) Search for something and click search icon
#3) Fetch title and URL







#############################################################################################3
## XPATH using attribute

'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[@href="/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles"]').click()

'''

## TASK

#1) Open youtube
#2) Search for anything and click search icon

'''
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys('tom and jerry')
driver.find_element(By.XPATH,'//button[@aria-label="Search"]').click()

'''



## TASK

#1) Open https://demoqa.com/text-box
#2) Fill the test fields and click on submit button



#######################################################################################
## XPATH by text

'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[.="New Releases"]').click()

'''


## Xpath by group by index
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[@class="nav-a  "])[7]').click()
sleep(3)
driver.find_element(By.XPATH,'(//a[@class="a-color-base a-link-normal"])[5]').click()

'''
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[text()="Bestsellers"])[1]').click()
sleep(2)
driver.find_element(By.XPATH,'(//div[@class="p13n-sc-uncoverable-faceout"])[4]').click()
sleep(6)
driver.find_element(By.ID,'add-to-cart-button').click()
'''



## TASK

#1) Open https://www.decathlon.in/
#2) Click on Hiking and Trekking
#3) Click on a product using group by index


'''
driver.get('https://www.decathlon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[@href="/shop/hiking-trekking-store"]').click()
sleep(3)
driver.find_element(By.XPATH,'(//a[@data-test-id="product-card-link"])[8]').click()
'''


###################################################################################3
## xpath using contains attribute
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[contains(@href,"/electronics")]').click()

'''

'''
driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'(//a[contains(@href,"/toys")])[1]').click()
sleep(2)
driver.find_element(By.XPATH,'(//a[contains(@href,"/gifting-store")])[2]').click()
sleep(2)
driver.find_element(By.XPATH,'//a[contains(@href,"collection-tab-name=toys&param")]').click()
'''




## xpath using contains text
'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'//a[contains(text(),"Deals")]').click()

'''


## TASK

#1) Open Decathlon
#2) Click Hiking and Trekking -- contains attribute
#2) Click Backpack and Rucksacks -- contains text

'''
driver.get('https://www.decathlon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[contains(@href,"hiking-trekking")]').click()
sleep(2)
driver.find_element(By.XPATH,'//div[contains(text(),"Rucksacks")]').click()
'''


## TASK  -- use contains text/attribute

#1) Open Amazon
#2) click on new release
#3) Click Books
#4) Choose a book
#5) Fetch title


'''
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[contains(@href,"new-releases")])[1]').click()
sleep(2)
driver.find_element(By.XPATH,'//a[contains(@href,"new-releases/books/")]').click()
sleep(2)
driver.find_element(By.XPATH,'(//div[contains(text(),"NCERT")])[1]').click()
sleep(2)
print(driver.title)

driver.quit()
'''

'''
driver.get('file:///C:/Users/Qsp/Desktop/HTML/Movie.html')
driver.maximize_window()
sleep(2)
# coll = driver.find_element(By.XPATH,'//td[text()="Vikram"]/../td[4]')
# print(coll.text)

name = driver.find_element(By.XPATH,'//td[text() = "800 CR"]/../td[2]')
print(name.text)
coll = driver.find_element(By.XPATH,'//td[text() = "800 CR"]')
print(coll.text)

## Fetch name of movie at SNO 4

## Fetch name of movie with collection 800 CR

'''




## Age of Cieera
## Salary of Cieera
## Department of Cieera

'''
driver.get('https://demoqa.com/webtables')
driver.maximize_window()
sleep(2)
age = driver.find_element(By.XPATH , '//td[text()="Cierra"]/../td[3]')
print("Age : ",age.text)
salary = driver.find_element(By.XPATH,'//td[text()="Cierra"]/../td[5]')
print("Salary : ",salary.text)
dept = driver.find_element(By.XPATH,'//td[text()="Cierra"]/../td[6]')
print("Dept : ",dept.text)

'''



## TASK

#1) Open https://www.prokabaddi.com/standings
#2) For a team name:
#   i) Find matches played
#   ii) Find matches won
#   iii) Find matches lost
#   iv) Find score difference
#   v) Find total points


'''
driver.get('https://www.prokabaddi.com/standings')
driver.maximize_window()
sleep(2)
matches_played = driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../..//div[@class="table-data matches-play"]/p')
matcher_won = driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../..//div[@class="table-data matches-won"]')
matches_lost = driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../..//div[@class="table-data matches-lost"]')
score_diff = driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../..//div[@class="table-data score-diff"]')
pts = driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../..//div[@class="table-data points"]')


print("Matches played : ",matches_played.text)
print("Matches won : ",matcher_won.text)
print("Matches lost : ",matches_lost.text)
print("Score diff : ",score_diff.text)
print("Points : ",pts.text)

driver.quit()

'''








## Xpath using sibling
driver.get('https://demoqa.com/webtables')
driver.maximize_window()
sleep(2)
sal = driver.find_element(By.XPATH,'//td[text()="Vega"]/following-sibling::td[3]')
print("Salary : ",sal.text)
fname = driver.find_element(By.XPATH,'//td[text()="Vega"]/preceding-sibling::td')
print("First Name : ",fname.text)
driver.quit()











