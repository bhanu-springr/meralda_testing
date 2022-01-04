from selenium import webdriver
import time

driver = webdriver.Chrome("C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
with open('contact_us'+'.txt', 'w+') as f:
    f.write("TESTING CONTACT US")
    
def contact_us():
    
    #scroll to bottom of webpage
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    contact = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[5]/a")
    contact.click()
    time.sleep(1)
    with open('contact_us'+'.txt', 'a') as f:
        text_1 = ("url of Contact Us page is : ",driver.current_url)
        text_1 = str(text_1)
        f.write("\n"+text_1)
    time.sleep(1)
    with open('contact_us'+'.txt', 'a') as f:
        text_2 = ("title of Contact Us page is : ", driver.title)
        text_2 = str(text_2)
        f.write("\n"+text_2)
    time.sleep(1)
try:
    contact_us()
    driver.close()
except:
    contact_us()
    driver.close()