#!/usr/local/bin/python3

from TestCase import TestCase

class WasRun(TestCase):

    def testMethod(self):
        self.log = self.log + 'testMethod '

    def setUp(self):
        self.log = 'setUp '

    def tearDown(self):
        self.log = self.log + 'tearDown '
