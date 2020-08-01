'''
Created on 01-Aug-2020

@author: 600031680
'''
import unittest
from testcases.NewTest5 import NewTest5
from testcases.NewTest6 import NewTest6
from testcases.POMNewTest13 import TestPOM
import HtmlTestRunner
from unittest.test import loader



Loader = unittest.TestLoader()
suite=unittest.TestSuite()

suite.addTest(Loader.loadTestsFromTestCase(NewTest5))
suite.addTest(Loader.loadTestsFromTestCase(NewTest6))
suite.addTest(Loader.loadTestsFromTestCase(TestPOM))

runner=HtmlTestRunner.HTMLTestRunner(output="./reports/",report_title='Test Practice Report')
runner.run(suite)