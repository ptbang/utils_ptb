import unittest
from unittest.main import main
#from utils_ptb import slownie
from context import slownie

class TestSlownie(unittest.TestCase):
    def test_kwota_slownie_odmiany(self):
        data = (
            (1, 'jeden złoty'),
            (1000002, 'jeden milion dwa złote'),
            (1000005, 'jeden milion pięć złotych'),
            (1456981, 'jeden milion czterysta pięćdziesiąt sześć tysięcy dziewięćset osiemdziesiąt jeden złotych'),
        )
        for d in data:
            self.assertEqual(slownie.kwota_slownie(d[0]), d[1])

    def test_kwota_slownie_negative(self):
        data = (
            (-1, 'minus jeden złoty'),
            (-1000002, 'minus jeden milion dwa złote'),
            (-1000005, 'minus jeden milion pięć złotych'),
            (-1456981, 'minus jeden milion czterysta pięćdziesiąt sześć tysięcy dziewięćset osiemdziesiąt jeden złotych'),
        )
        for d in data:
            self.assertEqual(slownie.kwota_slownie(d[0]), d[1])

    def test_kwota_slownie_decimal(self):
        data = (
            (-1.0, 'minus jeden złoty'),
            (-1000002.20, 'minus jeden milion dwa złote dwadzieścia groszy'),
            (1000005.01, 'jeden milion pięć złotych jeden grosz'),
            (1456981.14, 'jeden milion czterysta pięćdziesiąt sześć tysięcy dziewięćset osiemdziesiąt jeden złotych czternaście grosze'),
        )
        for d in data:
            self.assertEqual(slownie.kwota_slownie(d[0]), d[1])
            

if __name__ == "__main__":
    unittest.main()