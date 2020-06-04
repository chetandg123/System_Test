import time
import unittest

class Password(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("password changed")

    def tearDown(self):
        time.sleep(15)