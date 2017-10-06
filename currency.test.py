import currency
import unittest

class CurrencyTest(unittest.TestCase):
    def test_validCurrency(self):
        self.assertEqual(currency.isValidCurrency('USD'), True)
        self.assertEqual(currency.isValidCurrency('GBP'), True)
        self.assertEqual(currency.isValidCurrency('EURO'), True)
        self.assertEqual(currency.isValidCurrency('AUD'), True)

    def test_invalidCurrency(self):
        self.assertEqual(currency.isValidCurrency('JPY'), False)

    def test_convertCurrency(self):
        
        self.assertEqual(currency.convertCurrency('USD','EURO', 100), (1/1.176)*100)
    
    def test_falseConvertCurrency(self):
        self.assertEqual(currency.convertCurrency('JPY', 'CHF', 100), False)

    def test_convertCurrencies(self):
        self.assertEqual(currency.test_convertCurrencies('EURO', 100), ) #trying to figure out how the proper attribute to prove this works.

if __name__ == '__main__':
    unittest.main()