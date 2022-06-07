import unittest
from logic import get_today
from datetime import date



class SampleTest(unittest.TestCase):
    def test_today(self):
        correct_day = date.today().strftime("%d/%m/%Y88")
        estimated_day = get_today()
        self.assertEqual(correct_day, estimated_day)
