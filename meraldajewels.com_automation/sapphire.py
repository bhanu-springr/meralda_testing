from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def sapphire():
    with open('sapphire'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY STONE > SAPPHIRE")
    # click on jewellery then on Sapphire
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    sapphire = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[3]/li[5]/a")
    sapphire.click()
    time.sleep(1)
    url = ("url for sapphire page is :", driver.current_url)
    title = ("title for sapphire page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("sapphire"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    sapphire()
except:
    with open("sapphire"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()
    