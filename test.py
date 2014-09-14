from main import BBRepoTest, BBErrorException
import unittest

class TestBB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_dyndns_class(self):
        bb = BBRepoTest(5, 6)
        self.assertEqual(bb.sum(), 11)