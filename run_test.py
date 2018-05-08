"""Run all test."""
from test_case.CreateAsmtTest import CreateAsmtTest
import unittest
from HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
suite.addTest(CreateAsmtTest("test_gp_asmt_create"))

fp = open('./result.html', 'wb')
runner = HTMLTestRunner(stream = fp, title = 'create gp test report', description = 'test case execute result: ')
#runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()

