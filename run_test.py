"""Run all test."""
from test_case.CreateAsmtTest import CreateAsmtTest

# from test_case.DeleteAsmtTest import DeleteAsmtTest

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

suite = unittest.TestSuite()

#suite.addTest(CreateAsmtTest("test_gp_asmt_create"))
suite.addTest(CreateAsmtTest("test_ip_asmt_create"))
#suite.addTest(CreateAsmtTest("test_qa_asmt_create"))
# suite.addTest(DeleteAsmtTest("test_execute_delete"))

# Capture current time by some format"
now = time.strftime("%Y-%m-%d %H_%M_%H_%S")

# Identify the save path of report
filename = './' + now + 'result.html'
fp = open('./report/' + filename, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='Test Result: create 3 types of assignment',
    description='test case execute result: '
)
# runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()
