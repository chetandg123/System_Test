import time
import unittest

class SAR(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("Number of students is displayed on student attendance")

    def tearDown(self):
        time.sleep(15)