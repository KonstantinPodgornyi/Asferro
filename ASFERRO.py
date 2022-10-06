
import selenium
from selenium import webdriver
import requests
import time
import random


try:
    #connect the driver, go to the mail and log in

    link='https://www.google.com/intl/ru/gmail/about/'
    browser= webdriver.Chrome()
    browser.get(link)
    button1= browser.find_element_by_xpath("/html/body/header/div/div/div/a[2]").click()
    val1='danubiusrakocziut90@gmail.com'
    val2='kulturazvuka'
    button2= browser.find_element_by_id("identifierId" ).send_keys(val1)
    browser.find_element_by_css_selector('[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()


    time.sleep(2)
    button2= browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(val2)
    browser.find_element_by_xpath('//*[text()="Далее"]').click()


    time.sleep(2)
    button3= browser.find_element_by_css_selector('[class="T-I T-I-KE L3" ]').click()







    #get the identifier and switch the driver to the current window
    time.sleep(4)
    discr= browser.current_window_handle
    print(discr)
    browser.window_handles
    browser.switch_to.window(discr)

    #write a generator that enters an arbitrary digital value in the text of the letter
    sumbol=str([random.randint(i,10) for i in range(1, 11)])

    #enter value and send email
    browser.find_element_by_css_selector('[class="agP aFw" ]').send_keys('danubiusrakocziut90.2@gmail.com')
    browser.find_element_by_css_selector('[class="aoT" ]').send_keys(sumbol)
    browser.find_element_by_css_selector('[class="Am Al editable LW-avf tS-tW" ]').send_keys(sumbol)
    button4=browser.find_element_by_css_selector('[class="T-I J-J5-Ji aoO v7 T-I-atl L3" ]').click()



    #go to another mail and check for the presence of a letter
    time.sleep(2)
    link = 'https://www.google.com/intl/ru/gmail/about/'
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_xpath("/html/body/header/div/div/div/a[2]").click()
    val1 = 'danubiusrakocziut90.2@gmail.com'
    val2 = 'kulturazvuka2'
    button5 = browser.find_element_by_id("identifierId").send_keys(val1)
    browser.find_element_by_css_selector('[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()


    time.sleep(2)

    button6 = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(val2)
    browser.find_element_by_xpath('//*[text()="Далее"]').click()
    button7 = browser.find_element_by_xpath('//*[@id=":96"]/div/div[2]/span/a').click()


    # get text of a letter
    mail_text= browser.find_element_by_css_selector('[class="y2" ]').text

    # check text
    print(mail_text)


    #form a dictionary if necessary
    mail_info =dict()


finally:
     time.sleep(100)
     browser.quit()