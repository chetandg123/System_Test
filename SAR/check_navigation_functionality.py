import time
import unittest

class SAR(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("naviagation functionlity is working")

    def tearDown(self):
        time.sleep(15)