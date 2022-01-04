from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def colored_gem():
    with open('colored_gem'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY STONE > COLORED GEMSTONES")
    # click on jewellery then on colored_gem
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    colored_gem = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[3]/li[3]/a")
    colored_gem.click()
    time.sleep(2)
    url = ("url for Colored Gemstones page is :", driver.current_url)
    title = ("title for Colored Gemstones page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("colored_gem"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    colored_gem()
except:
    with open("colored_gem"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()