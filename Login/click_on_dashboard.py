import time
import unittest

class Dashboar(unittest.TestCase):
    def setUp(self):
        time.sleep(30)

    def test_query(self):
        print("Dashboard is displayed")

    def tearDown(self):
        time.sleep(30)
