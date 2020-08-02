'''
Created on Jun 16, 2020

@author: aswani.kumar.avilala
'''
import unittest
from testcases.DriverUtility import Drivers
from time import sleep


class NewTest5(unittest.TestCase):


    def testName(self):
        driver=Drivers.get_Browser_Instance(self, 'chrome')
        driver.get('https://www.hdfcbank.com/')
        driver.implicitly_wait(10)
        deposits=driver.find_element_by_xpath("//li[contains(text(),'Deposits')]")
        driver.execute_script("arguments[0].click();",deposits)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #driver.find_element_by_xpath("//li[contains(text(),'Deposits')]").click()
        print("Test Pass successfully")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()