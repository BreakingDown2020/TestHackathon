from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
def setUp():
    browser = webdriver.Firefox()
    browser.get("https://www.makemytrip.com/")
    browser.implicitly_wait(20)
    browser.find_element_by_xpath("//p[contains(.,'Login or Create Account')]").click()
    browser.find_element_by_id("username").send_keys("come002@gmail.com")
    options = browser.find_element_by_xpath("//span[contains(text(), 'Continue')]")
    if options.is_enabled():
        options.click()
    options = browser.find_element_by_xpath('//*[@id="SW"]/div[2]/div[2]/div[2]/section/form/div[2]/button')
    if options.is_enabled():
        options.click()
    browser.find_element_by_id("password").send_keys("amit0101@")
    browser.find_element_by_xpath('//button[@data-cy="login"]').click()
    browser.find_element_by_xpath('//span[@data-cy="modalClose"]').click()
    #time.sleep(5)
def hotel():
    browser = webdriver.Firefox()
    browser.get("https://www.makemytrip.com/")
    browser.implicitly_wait(20)
    browser.find_element_by_xpath("//span[@class='chNavIcon appendBottom2 chSprite chHotels']").click()
    browser.find_element_by_id('city').click()
    location = browser.find_element_by_xpath("//input[@placeholder='Enter city/ Hotel/ Area/ Building']")
    location.send_keys("Bangalore")
    my_select = Select(browser.find_element_by_xpath("//input[@placeholder='Enter city/ Hotel/ Area/ Building']"))
    my_select.select_by_index(1)
    time.sleep(2)
    browser.close()
if __name__=='__main__':
    setUp()
