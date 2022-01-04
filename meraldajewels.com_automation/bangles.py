from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def bangles():
    with open('bangles'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY CATEGORY > BANGLES")
    # click on jewellery then on bangles
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    bangles = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[1]/li[5]/a")
    bangles.click()
    time.sleep(2)
    url = ("url for Bangles page is :", driver.current_url)
    title = ("title Bangles Edit page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("bangles"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    bangles()
except:
    with open("bangles"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()