import time
import unittest

class UserCreate(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("User is created")

    def tearDown(self):
        time.sleep(15)
