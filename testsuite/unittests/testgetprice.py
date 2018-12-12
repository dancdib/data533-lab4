import unittest
from cadtax.calculator import taxcalculator as objpr
from cadtax.ratesframe import giverates as txr

class testGetPrice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupGetPrice")

    def setUp(self):
        print("Set up")
        self.testobj = objpr.objectprice('apple',2,'bc')

    def test_get_price(self):
        self.assertEqual(self.testobj.getprice(),2.24)

    unittest.main(argv=[''], verbosity=2, exit=False)

    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print('tearDownGetPrice')
