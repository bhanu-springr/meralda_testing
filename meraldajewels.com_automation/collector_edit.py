from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def collector_edit():
    with open('collector_edit'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > CURATED SHOPS > COLLECTOR'S EDIT")
    # click on jewellery then on collector_edit
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    collector_edit = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[4]/li[2]/a")
    collector_edit.click()
    time.sleep(2)
    url = ("url for Collector's Edit page is :", driver.current_url)
    title = ("title for Collector's Edit page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("collector_edit"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    collector_edit()
except:
    with open("collector_edit"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()