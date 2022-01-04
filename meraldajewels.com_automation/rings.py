from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def rings():
    with open('rings'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY CATEGORY > RINGS")
    # click on jewellery then on rings
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    rings = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[1]/li[3]/a")
    rings.click()
    time.sleep(2)
    url = ("url for rings page is :", driver.current_url)
    title = ("title for rings page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("rings"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    rings()
except:
    with open("rings"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()