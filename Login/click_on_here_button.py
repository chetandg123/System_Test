import time
import unittest

class ClickHere(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("Navigated to Regular User")

    def tearDown(self):
        time.sleep(15)
