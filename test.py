from main import BBRepoTest, BBErrorException
import unittest

class TestBB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum(self):
        bb = BBRepoTest(5, 6)
        self.assertEqual(bb.sum(), 11)

    def test_mul(self):
        bb = BBRepoTest(5, 5)
        self.assertEqual(bb.mul(), 25)