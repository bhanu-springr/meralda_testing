from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def estelle():
    with open('estelle'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY COLLECTION > ESTELLE")
    # click on jewellery then on estelle
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    estelle = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[2]/li[2]/a")
    estelle.click()
    time.sleep(2)
    url = ("url for estelle page is :", driver.current_url)
    title = ("title for estelle page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("estelle"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    estelle()
except:
    with open("estelle"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()