'''
Created on Jun 17, 2020

@author: aswani.kumar.avilala
'''
from selenium.webdriver.common.by import By

class WelcomePageDemoWebShop(object):
    '''
    classdocs
    '''
    REGISTER_LINK=(By.LINK_TEXT,'Register')
    LOGIN_LINK=(By.LINK_TEXT,'Log in')
    
    def click_register_link(self):
        self.driver.find_element(*WelcomePageDemoWebShop.REGISTER_LINK).click()
        return self.driver.title
        #self.driver.find_element(by=By.LINK_TEXT,'register').click()
        #self.driver.find_element_by_link_text('Register').click()
    def click_login_link(self):
        self.driver.find_element(*WelcomePageDemoWebShop.LOGIN_LINK).click()
        return self.driver.title
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver=driver
        
        