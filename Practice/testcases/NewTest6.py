'''
Created on Jun 16, 2020

@author: aswani.kumar.avilala
'''
import unittest
from testcases.DriverUtility import Drivers
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NewTest6(unittest.TestCase):


    def testName(self):
        driver=Drivers.get_Browser_Instance(self, 'chrome')
        driver.get('https://demos.telerik.com/aspnet-ajax/treeview/examples/overview/defaultcs.aspx')
        driver.implicitly_wait(10)
        sleep(5)
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        fromelement=driver.find_element_by_xpath("//div[@id='ctl00_ContentPlaceholder1_RadTreeView1']/ul/li/ul/li[3]/ul/li[1]/div/div/span")
        toelement=driver.find_element_by_id('ctl00_ContentPlaceholder1_priceChecker')
        actions=ActionChains(driver)
        actions.click_and_hold(fromelement).pause(3).release(toelement).perform()
        actions.drag_and_drop(fromelement,toelement).perform()
        flag=WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,'ctl00_ContentPlaceholder1_Label1'), "The price of 'Weekend Package' is : $3999"))
        self.assertTrue(flag,'the condition is failed')
        pricemessage=driver.find_element_by_id('ctl00_ContentPlaceholder1_Label1').text
        print(pricemessage)
        self.assertEqual(pricemessage,"The price of 'Weekend Package' is : $3999",'The message is not verified')
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()