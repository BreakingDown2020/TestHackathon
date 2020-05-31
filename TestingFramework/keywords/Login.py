import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import re

class MakeMyTrip(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.makemytrip.com/")
        self.browser.implicitly_wait(20)
        self.browser.find_element_by_xpath("//p[contains(.,'Login or Create Account')]").click()
        self.browser.find_element_by_id("username").send_keys("come002@gmail.com")
        options = self.browser.find_element_by_xpath("//span[contains(text(), 'Continue')]")
        if options.is_enabled():
            options.click()
        options = self.browser.find_element_by_xpath('//*[@id="SW"]/div[2]/div[2]/div[2]/section/form/div[2]/button')
        if options.is_enabled():
            options.click()
        self.browser.find_element_by_id("password").send_keys("amit0101@")
        self.browser.find_element_by_xpath('//button[@data-cy="login"]').click()
        self.browser.find_element_by_xpath('//span[@data-cy="modalClose"]').click()
        sleep(5)
    #def test_hotel_search(self):
        self.browser.find_element_by_xpath('//a[@href="https://www.makemytrip.com/hotels/"]').click()
        self.browser.find_element_by_id('city').click()
        location = self.browser.find_element_by_xpath("//input[@placeholder='Enter city/ Hotel/ Area/ Building']")
        city = "Bengaluru"
        location.send_keys(city)
        #sleep(5)
        sleep(1)
        self.browser.find_element_by_id("react-autowhatever-1-section-0-item-0").click()
        #WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-autowhatever-1']"))).send_keys(Keys.DOWN,Keys.RETURN, Keys.TAB)
        startdate = "25/12/2020"
        enddate = "2/02/2021"
        startdays = startdate.split('/')
        enddays = enddate.split('/')
        self.browser.find_element_by_id("checkin").click()
        currentyear = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div/span)[1]').get_attribute('innerText')
        while currentyear != startdays[2]:
            self.browser.find_element_by_class_name("DayPicker-NavButton.DayPicker-NavButton--next").click()
            currentyear = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div/span)[1]').get_attribute('innerText')
        currentmonth = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div)[1]').get_attribute('innerText')
        while "December" not in currentmonth:
            self.browser.find_element_by_class_name("DayPicker-NavButton.DayPicker-NavButton--next").click()
            currentmonth = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div)[1]').get_attribute('innerText')
        self.browser.find_element_by_xpath('//div[@class="DayPicker-Day"][text()="'+startdays[0]+'"]').click()
        currentyear = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div/span)[2]').get_attribute('innerText')
        while currentyear != enddays[2]:
            self.browser.find_element_by_class_name("DayPicker-NavButton.DayPicker-NavButton--next").click()
            currentyear = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div/span)[2]').get_attribute('innerText')
        currentmonth = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div)[2]').get_attribute('innerText')
        while "February" not in currentmonth:
            self.browser.find_element_by_class_name("DayPicker-NavButton.DayPicker-NavButton--next").click()
            currentmonth = self.browser.find_element_by_xpath('(//div[@class="DayPicker-Caption"]/div)[2]').get_attribute('innerText')
        self.browser.find_element_by_xpath('(//div[@class="DayPicker-Day"][text()="'+enddays[0]+'"])[2]').click()
    def test_Date_Picker(self):
        self.browser.find_element_by_xpath("//input[@id='guest']").click()
        num_of_adults = 2
        total_adult = 'adults-'+str(num_of_adults)
        keyword = "//li[@data-cy="+"'"+total_adult+"'"+"]"
        self.browser.find_element_by_xpath(keyword).click()
        total_child = 'children-'+str(num_of_adults)
        keyword1 = "//li[@data-cy="+"'"+total_child+"'"+"]"
        self.browser.find_element_by_xpath(keyword1).click()
        self.browser.find_element_by_xpath("//button[@data-cy='addAnotherRoom']").click()
        self.browser.find_element_by_xpath(keyword).click()
        self.browser.find_element_by_xpath(keyword1).click()
        self.browser.find_element(By.XPATH, "//button[@data-cy='submitGuest']").click()
        self.browser.find_element_by_xpath("//p[@data-cy='travelForReasonTxt']").click()
        tr_reason = "travelFor-"+"work".capitalize()
        keyword2 = "//li[@data-cy="+"'"+tr_reason+"'"+"]"
        self.browser.find_element_by_xpath(keyword2).click()
        sleep(2)
        self.browser.find_element_by_id("hsw_search_button").click()
        sleep(5)
    def tearDown(self):
        self.browser.close()
if __name__=='__main__':
    unittest.main()


