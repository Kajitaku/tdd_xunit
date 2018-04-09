#!/usr/local/bin/python3

from TestCase import TestCase

class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasSetUp = 1
