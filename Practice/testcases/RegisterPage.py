'''
Created on Jun 17, 2020

@author: aswani.kumar.avilala
'''
from selenium.webdriver.common.by import By
from asyncio.tasks import sleep


class RegisterPageDemoWebShop(object):
    '''
    classdocs
    '''
    GENDER=(By.ID,'gender-male')
    FIRST_NAME=(By.ID,'FirstName')
    LAST_NAME=(By.ID,'LastName')
    EMAIL_ID=(By.ID,'Email')
    PASSWORD=(By.ID,'Password')
    CNF_PASSWORD=(By.ID,'ConfirmPassword')
    REGISTER=(By.ID,'register-button')
    
    def click_register_button(self):
        self.driver.find_element(*RegisterPageDemoWebShop.GENDER).click()
        self.driver.find_element(*RegisterPageDemoWebShop.FIRST_NAME).send_keys('aswani')
        self.driver.find_element(*RegisterPageDemoWebShop.LAST_NAME).send_keys('kumar')
        self.driver.find_element(*RegisterPageDemoWebShop.EMAIL_ID).send_keys('aswani@test.com')
        self.driver.find_element(*RegisterPageDemoWebShop.PASSWORD).send_keys('abc123')
        self.driver.find_element(*RegisterPageDemoWebShop.CNF_PASSWORD).send_keys('abc123')
        sleep(5)
        self.driver.find_element(*RegisterPageDemoWebShop.REGISTER).click()

      
    
    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver=driver