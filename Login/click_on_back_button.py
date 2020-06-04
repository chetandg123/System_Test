import time
import unittest

class OnRegularUser(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("Navigated to login page")

    def tearDown(self):
        time.sleep(15)
