#!/usr/local/bin/python3

from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert('setUp testMethod ' == test.log)

TestCaseTest("testTemplateMethod").run()
