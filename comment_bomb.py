#!/usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

selenium = webdriver.Chrome()

#driver = webdriver.Chrome('chromedriver')  # Optioznal argument, if not specified will search path.
selenium.get("https://www.page.com/contact")
count = 0 
while count < 2:
    count = count + 1
    print(count)


    comment = selenium.find_element_by_id("ContactForm-message")
    name = selenium.find_element_by_id("ContactForm-name")
    phone = selenium.find_element_by_id("ContactForm-phone")
    email = selenium.find_element_by_id("ContactForm-email")
     
    comment.send_keys("I would like to order")
    email.send_keys("ted@gmail.com")
    phone.send_keys("796-777-6979")
    name.send_keys("ted")
     
    selenium.find_element_by_css_selector('input[type="submit"]').submit()
    print("party time number" + "  " + str(count))
    time.sleep(15)
