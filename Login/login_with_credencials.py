import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("login successful")

    def tearDown(self):
        time.sleep(15)