import time
import unittest

class Semester(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("Semester map is displayed")

    def tearDown(self):
        time.sleep(15)