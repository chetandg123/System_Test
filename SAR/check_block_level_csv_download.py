import time
import unittest

class SAR(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("block wise csv downloaded")

    def tearDown(self):
        time.sleep(15)