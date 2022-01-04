from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def earrings():
    with open('earrings'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY CATEGORY > EARRINGS")
    # click on jewellery then on earrings
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    earrings = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[1]/li[4]/a")
    earrings.click()
    time.sleep(2)
    url = ("url for earrings page is :", driver.current_url)
    title = ("title for earrings page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("earrings"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    earrings()
except:
    with open("earrings"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()