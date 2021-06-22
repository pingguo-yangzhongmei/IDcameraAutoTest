import os
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
        suite = unittest.defaultTestLoader.discover(r'/Users/theblue/IDcameraAutoTest/teste_case', pattern='test*.py')
        result = BeautifulReport(suite)
        result.report(filename='测试报告', description='证件照', report_dir='test_report')
