import unittest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PerformanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    #time to load webpage using ip
    def test_perf_test_ip(self):
        start = datetime.now()
        self.driver.get("http://13.56.178.91/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"nginx.org")))
        end = datetime.now()
        perf = end - start
        print ("The page using ip address loaded in " + str(perf) + " seconds")

    #time to load webpage using domain
    def test_perf_test_domain(self):
        start = datetime.now()
        self.driver.get("http://www.aleena-nginxserver.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"nginx.org")))
        end = datetime.now()
        perf = end - start
        print ("The page using domain name loaded in " + str(perf) + " seconds")

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()