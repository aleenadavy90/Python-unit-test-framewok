import unittest
from NginxWebServerTest import WebServerTest
from NginxPerfTest import PerformanceTest

# get all tests from WebServerTest and PerformanceTest
WebServerTest = unittest.TestLoader().loadTestsFromTestCase(WebServerTest)
PerformanceTest = unittest.TestLoader().loadTestsFromTestCase(PerformanceTest)

# create a test suite combining WebServerTest and PerformanceTest
test_suite = unittest.TestSuite([WebServerTest,PerformanceTest])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)