from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def fiori():
    with open('fiori'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY COLLECTION > FIORI")
    # click on jewellery then on fiori
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    fiori = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[2]/li[4]/a")
    fiori.click()
    time.sleep(2)
    url = ("url for fiori page is :", driver.current_url)
    title = ("title for fiori page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("fiori"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    fiori()
except:
    with open("fiori"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()