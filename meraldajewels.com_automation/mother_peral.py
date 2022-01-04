from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def mother_pearl():
    with open('mother_pearl'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY STONE > MOTHER OF PEARL")
    # click on jewellery then on mother_pearl
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    mother_pearl = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[3]/li[6]/a")
    mother_pearl.click()
    time.sleep(2)
    url = ("url for mother of pearl page is :", driver.current_url)
    title = ("title for mother of pearl page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("mother_pearl"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    mother_pearl()
except:
    with open("mother_pearl"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()