"""Run all test."""
from test_case.CreateAsmtTest import CreateAsmtTest
import unittest


suite = unittest.TestSuite()
suite.addTest(CreateAsmtTest("test_gp_asmt_create"))


runner = unittest.TextTestRunner()
runner.run(suite)