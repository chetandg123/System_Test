import time
import unittest

class Semester(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("Districts are selected from select box")

    def tearDown(self):
        time.sleep(15)