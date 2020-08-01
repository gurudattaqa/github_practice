'''
Created on Jun 17, 2020

@author: aswani.kumar.avilala
'''
from selenium.webdriver.common.by import By

class LoginPageDemoWebShop(object):
    '''
    classdocs
    '''
    USER_ID=(By.ID,'Email')
    PASSWORD=(By.ID,'Password')
    LOGIN=(By.CSS_SELECTOR,"input[value='Log in']")

    def click_login_button(self):
        self.driver.find_element(*LoginPageDemoWebShop.USER_ID).send_keys('askmail@email.com')
        self.driver.find_element(*LoginPageDemoWebShop.PASSWORD).send_keys('abc123')
        self.driver.find_element(*LoginPageDemoWebShop.LOGIN).click()
        return self.driver.title
        
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver=driver