import unittest

from unittests.testaxcalc import testTaxCalc
from unittests.testgetprice import testGetPrice
from unittests.testtax import testRatesFrame
from unittests.testcalculator import testCalculator

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(Testtaxcalc))
    suite.addTest(unittest.makeSuite(TestGetPrice))
    suite.addTest(unittest.makeSuite(TestRatesFrame))
    suite.addTest(unittest.makeSuite(TestCalculator))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
