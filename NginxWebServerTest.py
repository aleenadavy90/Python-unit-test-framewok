import unittest
from selenium import webdriver

class WebServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    def test_nginx_ip_address_loads(self):
        # navigate to Nginx landing page using public IP address
        self.driver.get("http://13.56.178.91/")
        URL = self.driver.current_url
        self.assertEquals(URL, "http://13.56.178.91/")

    def test_nginx_domain_name_loads(self):
        # navigate to Nginx landing page using Domain name
        self.driver.get("http://www.aleena-nginxserver.com/")
        URL = self.driver.current_url
        self.assertEquals(URL, "http://www.aleena-nginxserver.com/")

    def test_text_exists_in_webpage(self):
        text = "Welcome to nginx!"
        self.assertTrue(text in self.driver.page_source)

    def test_page_loads_using_other_hostname(self):
        # navigate to Nginx landing page using other Domain names
        self.driver.get("http://test.aleena-nginxserver.com/")
        text = "Welcome to nginx!"
        self.assertTrue(text in self.driver.page_source)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()