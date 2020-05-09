#!/usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

selenium = webdriver.Chrome()

driver.get("http://mywebsite/about-2/")
count = 0 
while count < 666666666666666666666666666666666666666666666:
    count = count + 1
    print count


    comment = selenium.find_element_by_id("comment")
    author = selenium.find_element_by_id("author")
    email = selenium.find_element_by_id("email")
     
    comment.send_keys("this is message")
    email.send_keys(this@test.com")
    author.send_keys("señor. comentarista")
     
    selenium.find_element_by_name("submit").click()
    print("party time number" + "  " + count)
    time.sleep(5)
