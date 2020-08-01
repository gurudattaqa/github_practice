'''
Created on Jun 17, 2020

@author: Guru
'''
import unittest

from testcases.DriverUtility import Drivers
from testcases.WelcomePage import WelcomePageDemoWebShop
from testcases.RegisterPage import RegisterPageDemoWebShop
from testcases.LoginPage import LoginPageDemoWebShop


class TestPOM(unittest.TestCase):


    def setUp(self):
        self.driver=Drivers.get_Browser_Instance(self,'chrome')
        self.driver.get('http://demowebshop.tricentis.com/')
        self.driver.implicitly_wait(10)
        self.wcpage=WelcomePageDemoWebShop(self.driver)
        self.rgpage=RegisterPageDemoWebShop(self.driver)
        self.lgpage=LoginPageDemoWebShop(self.driver)
        pass


    def tearDown(self):
        pass
    '''
    def testDemoWebShopRegisterLink(self):
        title=self.wcpage.click_register_link()
        self.assertTrue('Register' in title)
        pass
    '''
    def testDemoWebSHopLoginLink(self):
        title=self.wcpage.click_login_link()
        self.assertTrue('Login' in title)
        titleb=self.lgpage.click_login_button()
        self.assertTrue('Demo Web Shop' in titleb)
    
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()