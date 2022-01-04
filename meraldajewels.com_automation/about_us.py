from selenium import webdriver
import time

driver = webdriver.Chrome("C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
with open('about_us'+'.txt', 'w+') as f:
    f.write("TESTING ABOUT US")
    
def about_us():
    
    #scroll to bottom of webpage
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    about = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[1]/a")
    about.click()
    time.sleep(1)
    with open('about_us'+'.txt', 'a') as f:
        text_1 = ("url of about us page is : ",driver.current_url)
        text_1 = str(text_1)
        f.write("\n"+text_1)
    time.sleep(1)
    with open('about_us'+'.txt', 'a') as f:
        text_2 = ("title of about us page is : ", driver.title)
        text_2 = str(text_2)
        f.write("\n"+text_2)
    time.sleep(1)
try:
    about_us()
    driver.close()
except:
    about_us()
    driver.close()