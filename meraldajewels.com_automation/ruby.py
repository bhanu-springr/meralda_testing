from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
url = "http://www.meraldajewels.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

def ruby():
    with open('ruby'+'.txt', 'w+') as f:
        f.write("TESTING JEWELLERY > BY STONE > RUBY")
    # click on jewellery then on ruby
    jewellery = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/a")
    jewellery.click()
    time.sleep(2)
    ruby = driver.find_element_by_xpath("//*[@id='homeMainnavBarDrop']/div/ul/li[2]/div/div/div/ul[3]/li[4]/a")
    ruby.click()
    time.sleep(2)
    url = ("url for ruby page is :", driver.current_url)
    title = ("title for ruby page is :", driver.title)
    url = str(url)
    title = str(title)
    with open("ruby"+".txt",'a') as f:
        f.write("\n"+ url)
        f.write("\n"+ title)
    driver.close()

try:
    ruby()
except:
    with open("ruby"+".txt",'a') as f:
        f.write("\n unable to fetch url and title or load the page")
        driver.close()