from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def hues():
    with open('hues'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY COLLECTION > HUES")
    # click on jewellery then on hues
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    hues = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[2]/li[3]/a")
    hues.click()
    time.sleep(2)
    url = ("url for hues page is :", driver.current_url)
    title = ("title for hues page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("hues"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    hues()
except:
    with open("hues"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()