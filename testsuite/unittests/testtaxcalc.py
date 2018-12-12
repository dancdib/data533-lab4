import unittest
from cadtax.calculator import taxcalculator as objpr
from cadtax.ratesframe import giverates as txr

class testTaxCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupGetPrice")

    def setUp(self):
        print("Set up")
        self.testobj = objpr.calctax('apple',2,'bc')

    def test_tax(self):
        self.assertEqual(self.testobj.tax(),2.24)

    unittest.main(argv=[''], verbosity=2, exit=False)

    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print('tearDownCalculator')
