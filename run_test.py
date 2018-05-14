"""Run all test."""
from test_case.CreateAsmtTest import CreateAsmtTest
<<<<<<< HEAD
#from test_case.DeleteAsmtTest import DeleteAsmtTest
=======
# from test_case.DeleteAsmtTest import DeleteAsmtTest
>>>>>>> 59074e7f59447a21b702d94bcf46cac3c383933e
import unittest
from HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
<<<<<<< HEAD
#suite.addTest(CreateAsmtTest("test_gp_asmt_create"))
suite.addTest(CreateAsmtTest("test_ip_asmt_create"))
#suite.addTest(CreateAsmtTest("test_qa_asmt_create"))
#suite.addTest(DeleteAsmtTest("test_execute_delete"))
=======
# suite.addTest(CreateAsmtTest("test_gp_asmt_create"))
suite.addTest(CreateAsmtTest("test_ip_asmt_create"))
# suite.addTest(CreateAsmtTest("test_qa_asmt_create"))
# suite.addTest(DeleteAsmtTest("test_execute_delete"))
>>>>>>> 59074e7f59447a21b702d94bcf46cac3c383933e

fp = open('./result.html', 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='create 3 types of assignment',
    description='test case execute result: '
)
# runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()
