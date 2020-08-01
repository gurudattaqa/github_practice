'''
Created on Jun 15, 2020

@author: aswani.kumar.avilala
'''
from selenium import webdriver

class Drivers(object):
    '''
    this class is to show the drivers configuration
    classdocs
    '''
    @staticmethod
    def get_Browser_Instance(self,browserName):
        if browserName == 'chrome':
            chrome_driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
            chrome_driver.maximize_window()
            return chrome_driver
        elif browserName == 'firefox':
            firefox_driver=webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
            firefox_driver.maximize_window()
            return firefox_driver
        elif browserName == 'ie':
            ie_driver=webdriver.Ie(executable_path='../drivers/IEDriverServer.exe')
            ie_driver.maximize_window()
            return ie_driver
        else:
            return None
        
    