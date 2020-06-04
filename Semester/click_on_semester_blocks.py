import time
import unittest

class Semester(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("clicked on block button")

    def tearDown(self):
        time.sleep(15)