import time
import unittest

class Sem(unittest.TestCase):
    def setUp(self):
        time.sleep(15)

    def test_query(self):
        print("cluster wise csv downloaded")

    def tearDown(self):
        time.sleep(15)