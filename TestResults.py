import unittest
import os

from HtmlTestRunner import HTMLTestRunner

from NginxWebServerTest import WebServerTest
from NginxPerfTest import PerformanceTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from WebServerTest and PerformanceTest class
web_server_test = unittest.TestLoader().loadTestsFromTestCase(WebServerTest)
perf_test = unittest.TestLoader().loadTestsFromTestCase(PerformanceTest)

# create a test suite combining WebServerTest and PerformanceTest
test_suite = unittest.TestSuite([WebServerTest,PerformanceTest])

# open the report file
outfile = open(dir + "\NginxWebServerTestSummary.html", "wb")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
