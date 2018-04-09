#!/usr/local/bin/python3

from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):

    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.WasRun)

TestCaseTest("testRunning").run()
