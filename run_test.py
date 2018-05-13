"""Run all test."""
from test_case.CreateAsmtTest import CreateAsmtTest
# from test_case.DeleteAsmtTest import DeleteAsmtTest
import unittest
from HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
# suite.addTest(CreateAsmtTest("test_gp_asmt_create"))
suite.addTest(CreateAsmtTest("test_ip_asmt_create"))
# suite.addTest(CreateAsmtTest("test_qa_asmt_create"))
# suite.addTest(DeleteAsmtTest("test_execute_delete"))

fp = open('./result.html', 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='create 3 types of assignment',
    description='test case execute result: '
)
# runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()
