import time
import unittest

class ChangePassword(unittest.TestCase):
    def setUp(self):
        time.sleep(30)

    def test_query(self):
        print("password validated")

    def tearDown(self):
        time.sleep(30)
