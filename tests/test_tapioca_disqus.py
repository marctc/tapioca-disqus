# coding: utf-8

import unittest

from tapioca_disqus import Disqus


class TestTapiocaDisqus(unittest.TestCase):

    def setUp(self):
        self.wrapper = Disqus()


if __name__ == '__main__':
    unittest.main()
