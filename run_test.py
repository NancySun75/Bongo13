"""Run all test."""
from test_case.ExecuteAsmtTest import ExecuteAsmtTest
import unittest


suite = unittest.TestSuite()
suite.addTest(ExecuteAsmtTest("test_ip_asmt_execute"))

runner = unittest.TextTestRunner()
runner.run(suite)
