import unittest
from cadtax.calculator import taxcalculator as objpr
from cadtax.ratesframe import giverates as txr

class testCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupCalculator")

    #Creates object to test
    def setUp(self):
        print("Setup")
        self.testobj = objpr.objectprice('apple',2,'bc')

    #Test to make sure the parameters are being taken in correctly
    def test_item_params(self):
        self.assertEqual(self.testobj.name,'apple')
        self.assertEqual(self.testobj.price,2)
        self.assertEqual(self.testobj.prov,'bc')

    unittest.main(argv=[''], verbosity=2, exit=False)

    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print('tearDownCalculator')
