import unittest
from cadtax.calculator import taxcalculator as objpr
from cadtax.ratesframe import giverates as txr

class testRatesFrame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupRatesFrame")

    def setUp(self):
        print("Set up")
        self.testdf = txr.taxrates.displayrates()

    def test_dataframe(self):
        self.assertIsNotNone(self.testdf)

    unittest.main(argv=[''], verbosity=2, exit=False)

    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print('teardownRatesFrame')
