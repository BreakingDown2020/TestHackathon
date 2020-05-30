from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
def setUp():
    browser = webdriver.Firefox()
    browser.get("https://www.makemytrip.com/")
    browser.implicitly_wait(20)
    browser.find_element_by_xpath("//p[contains(.,'Login or Create Account')]").click()
    browser.find_element_by_id("username").send_keys("come002@gmail.com")
    time.sleep(3)
    browser.find_element_by_xpath("//span[contains(@class, 'capText font16' and text()='Continue']").click()
    browser.find_element_by_id("password").send_keys("amit0101@")
    browser.close()
def hotel():
    browser = webdriver.Firefox()
    browser.get("https://www.makemytrip.com/")
    browser.implicitly_wait(20)
    browser.find_element_by_xpath("//span[@class='chNavIcon appendBottom2 chSprite chHotels']").click()
    browser.find_element_by_id('city').click()
    my_select = Select(browser.find_element_by_xpath("//input[@placeholder='Enter city/ Hotel/ Area/ Building']").send_keys("Bangalore"))
    print(my_select)
    my_select.select_by_index(1)
    time.sleep(2)
    browser.close()
if __name__=='__main__':
    hotel()
