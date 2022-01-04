from selenium import webdriver
import time

driver = webdriver.Chrome("C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
with open('privacy_policy'+'.txt', 'w+') as f:
    f.write("TESTING PRIVACY POLICY")
    
def privacy_policy():
    
    #scroll to bottom of webpage
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    privacy = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[3]/a")
    privacy.click()
    time.sleep(1)
    with open('privacy_policy'+'.txt', 'a') as f:
        text_1 = ("url of Privacy Policy page is : ",driver.current_url)
        text_1 = str(text_1)
        f.write("\n"+text_1)
    time.sleep(1)
    with open('privacy_policy'+'.txt', 'a') as f:
        text_2 = ("title of Privacy Policy page is : ", driver.title)
        text_2 = str(text_2)
        f.write("\n"+text_2)
    time.sleep(1)
try:
    privacy_policy()
    driver.close()
except:
    privacy_policy()
    driver.close()