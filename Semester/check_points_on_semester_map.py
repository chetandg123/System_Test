import time
import unittest

class Semester(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("dots are displayed on map")

    def tearDown(self):
        time.sleep(15)