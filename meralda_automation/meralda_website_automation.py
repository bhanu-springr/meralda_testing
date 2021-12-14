# -*- coding: utf-8 -*-
"""
@author: bhanu
"""
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime
import requests
import time
now = datetime.now()
log_name = now.strftime(" %H%M%S_%d%m%Y")
print(log_name)
with open(log_name+'_meralda'+'.txt', 'w+') as f:
    f.write("meralda.scalenext.io TESTING LOG FILE :-")
    driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
    url = "http://meralda.scalenext.io/"
    driver.get(url)
    driver.maximize_window()
    # check if website loads successfully
    response = requests.get(url)    
    status = response.status_code
    if status == 200:
        #f.write("\nWebsite is working : PASSED")
        f.write("\n1. website loaded successfully")
    time.sleep(3)
    # check if user login successfully
    email = "123@123.com"
    password = "qwer12345"
    # click on profile logo
    profile = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/a")
    profile.click()
    time.sleep(1)
    if driver.current_url == "http://meralda.scalenext.io/user/login":
        f.write("\n2. login page open successfully")   
        time.sleep(1)
    #enter email and password
    e_mail = driver.find_element_by_xpath("//*[@id='shippingForm']/div[1]/div/div[1]/input")
    e_mail.send_keys(email)
    pass_word = driver.find_element_by_xpath("//*[@id='shippingForm']/div[1]/div/div[2]/input")
    pass_word.send_keys(password)
    login_btn = driver.find_element_by_xpath("//*[@id='shippingForm']/div[3]/button")
    login_btn.click()
    time.sleep(3)
    logo = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[1]/div[1]/div[1]/a/img")
    assert logo.is_displayed()==True
    f.write("\n3. login successfully and redirected to homepage")
    
    # check if meralda logo at homepage is clickable
    m_logo = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[1]/div[1]/div[1]/a/img")
    try:
        m_logo.click()
        f.write("\n4. meralda logo is clickable")
    except WebDriverException:
        f.write("\n4. Element is not clickable")
    time.sleep(3)
    # click on Home
    def home():
        home = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[1]/a")
        home.click()
        if driver.current_url == "http://meralda.scalenext.io/":
            f.write("\n5. redirected to homepage")
    home()
    time.sleep(3)
                    
    def jewellery():
        jewellery = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/a")
        jewellery.click()
    # checking all the dropdown of "By Category"
    # click on jewellery then on Necklace & Pendants
    jewellery()
    time.sleep(1)
    necklace_pendants = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[1]/li[2]/a")
    necklace_pendants.click()
    if driver.current_url == "http://meralda.scalenext.io/product-cat/necklaces-pendants":
        f.write("\n6. redirected to Necklace and Pendants webpage")
        time.sleep(3)
      
    # click on jewellery then on RIngs
    jewellery()
    time.sleep(1)
    rings = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[1]/li[3]/a")
    rings.click()
    if driver.current_url == "http://meralda.scalenext.io/product-cat/rings":
        f.write("\n7. redirected to Rings webpage")
        time.sleep(3)
       
    # click on jewellery then on Earrings
    jewellery()
    time.sleep(1)
    ear_rings = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[1]/li[4]/a")
    ear_rings.click()
    if driver.current_url == "http://meralda.scalenext.io/product-cat/earrings":
        f.write("\n8. redirected Earrings webpage")
        time.sleep(3)
      
    # click on jewellery then on Bangles
    jewellery()
    time.sleep(1)
    bangles = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[1]/li[5]/a")
    bangles.click()
    if driver.current_url == "http://meralda.scalenext.io/product-cat/bangles":
        f.write("\n9. redirected to Bangles webpage")
        time.sleep(3)
        
    # checking all the dropdown of "By Collection"
    # click on jewellery then on Estelle
    jewellery()
    time.sleep(1)
    estelle = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[2]/li[2]/a")
    estelle.click()
    if driver.current_url == "http://meralda.scalenext.io/product-collection/estelle":
        f.write("\n10. redirected to Estelle webpage")
        time.sleep(3)
        
    # click on jewellery then on Hues
    jewellery()
    time.sleep(1)
    hues = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[2]/li[3]/a")
    hues.click()
    if driver.current_url == "http://meralda.scalenext.io/product-collection/hues":
        f.write("\n11. redirected to Hues webpage")
        time.sleep(3)
    
    # click on jewellery then on Fiori
    jewellery()
    time.sleep(1)
    fiori = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[2]/li[4]/a")
    fiori.click()
    if driver.current_url == "http://meralda.scalenext.io/product-collection/fiori":
        f.write("\n12. redirected to Fiori webpage")
        time.sleep(3)
        
    # checking all the dropdown of "By Stone"
    # click on jewellery then on Diamond
    jewellery()
    time.sleep(1)
    diamond = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[3]/li[2]/a")
    diamond.click()
    if driver.current_url == "http://meralda.scalenext.io/product-stone/diamond":
        f.write("\n13. redirected to Diamond webpage")
        time.sleep(3)
    
    # click on jewellery then on Colored Gemstones
    jewellery()
    time.sleep(1)
    colored_gemstones = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[3]/li[3]/a")
    colored_gemstones.click()
    if driver.current_url == "http://meralda.scalenext.io/product-stone/colored-gemstones":
        f.write("\n14. redirected to Colorsed Gemstone webpage")
        time.sleep(3)
    
    # click on jewellery then on Ruby
    jewellery()
    time.sleep(1)
    ruby = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[3]/li[4]/a")
    ruby.click()
    if driver.current_url == "http://meralda.scalenext.io/product-stone/ruby":
        f.write("\n15. redirected to Ruby webpage")
        time.sleep(3)
    
    # click on jewellery then on Sapphire
    jewellery()
    time.sleep(1)
    sapphire = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[3]/li[5]/a")
    sapphire.click()
    if driver.current_url == "http://meralda.scalenext.io/product-stone/blue-sapphire":
        f.write("\n16. redirected to Sapphire webpage")
        time.sleep(3)
    
    # click on jewellery then on Mother of Pearl
    jewellery()
    time.sleep(1)
    mother_of_pearl = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[3]/li[6]/a")
    mother_of_pearl.click()
    if driver.current_url == "http://meralda.scalenext.io/product-stone/mother-of-pearl":
        f.write("\n17. redirected to Mother of Pearl webpage")
        time.sleep(3)
        
    # checking all dropdown of "Curated Shops"
    # click on jewellery then on Bridal Edit
    jewellery()
    time.sleep(1)
    bridal_edit = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[4]/li[2]/a")
    bridal_edit.click()
    if driver.current_url == "http://meralda.scalenext.io/product-collection/bridal-edit":
        f.write("\n18. redirected to Bridal Edit webpage")
        time.sleep(3)
        
    # click on jewellery then on Collector's Edit
    jewellery()
    time.sleep(1)
    bridal_edit = driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div[2]/div/ul/li[2]/div/div/div/ul[4]/li[3]/a")
    bridal_edit.click()
    if driver.current_url == "http://meralda.scalenext.io/product-collection/collectors-edit":
        f.write("\n19. redirected to Collector's Edit webpage")
        time.sleep(3)
    #scroll to bottom of webpage
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    about_us = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[1]/a")
    about_us.click()
    if driver.current_url == "http://meralda.scalenext.io/about-us":
        f.write("\n20. clicked on about us and redirected to about us webpage")
        time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    careers = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[2]/a")
    careers.click()
    if driver.current_url == "http://meralda.scalenext.io/career":
        f.write("\n21. clicked on careers and redirected to careers webpage")
        time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    privacy_policy = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[3]/a")
    privacy_policy.click()
    if driver.current_url == "http://meralda.scalenext.io/privacy-policy":
        f.write("\n22. clicked on privacy-policy and redirected to privacy-policy webpage")
        time.sleep(3)    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    terms_condition = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[4]/a")
    terms_condition.click()
    if driver.current_url == "http://meralda.scalenext.io/terms-condition":
        f.write("\n23. clicked on terms and condition and redirected to terms and condition webpage")
        time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    contact_us = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[2]/ul/li[5]/a")
    contact_us.click()
    if driver.current_url == "http://meralda.scalenext.io/contact":
        f.write("\n24. clicked on contact us and redirected to contact us webpage")
        time.sleep(3)
    # checking the social media links
    # scroll down to bottom of webpage and click on facebook logo
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    facebook = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[4]/ul[1]/li[1]/a")
    facebook.click()
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    time.sleep(1)
    if driver.current_url == "https://www.facebook.com/meraldajewels/":
        f.write("\n25. after click on FB logo it is redirected to fb page of meralda")
        driver.close()
    
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    instagram = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[4]/ul[1]/li[2]/a")    
    instagram.click()
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    time.sleep(1)
    # https://www.instagram.com/meralda.jewels/
    if driver.current_url == "https://www.instagram.com/accounts/login/":
        f.write("\n26. after click on Instagram logo it is redirected to Instagram page of meralda")
        driver.close()
        
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    pinterest = driver.find_element_by_xpath("//*[@id='app']/footer/div[1]/div/div/div[4]/ul[1]/li[3]/a")    
    pinterest.click()
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    time.sleep(1)
    if driver.current_url == "https://in.pinterest.com/meraldajewels/":
        f.write("\n27. after click on Pinterest logo it is redirected to Pinterest page of meralda")
        driver.close()
    # click on springr logo 
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    springr = driver.find_element_by_xpath("//*[@id='app']/footer/div[2]/div/p[2]/a")    
    springr.click()
    time.sleep(1)
    driver.switch_to.window(window_name = driver.window_handles[-1])
    time.sleep(1)
    if driver.current_url == "https://springr.in/":
        f.write("\n28. after click on springr logo it is redirected to springr website")
        driver.close()
        driver.close()