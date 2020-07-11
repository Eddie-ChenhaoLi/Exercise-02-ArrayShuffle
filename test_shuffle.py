import random
import unittest
import shuffle
from unittest import mock


class TestShuffle(unittest.TestCase):

    def test_generate_array(self):
        self.assertEqual(shuffle.generate_array(2, 5), [2, 3, 4])
        self.assertEqual(shuffle.generate_array(4, 8), [4, 5, 6, 7])

    def test_shuffle_array(self):
        random.shuffle = mock.Mock(return_value=[3, 2, 4])
        self.assertEqual(shuffle.shuffle_array([2, 3, 4]), [3, 2, 4])
        random.shuffle = mock.Mock(return_value=[6, 5, 4, 7])
        self.assertEqual(shuffle.shuffle_array([4, 5, 6, 7]), [6, 5, 4, 7])
