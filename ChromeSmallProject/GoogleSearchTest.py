from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_search_automation(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.NAME, 'q').send_keys("Automation step by step")
        self.driver.find_element(By.NAME, "btnK").click()
    def test_search_sudip(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.NAME, 'q').send_keys("sudipto naskar")
        self.driver.find_element(By.NAME, "btnK").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("test completed")
#open cmd and run "cd C:\Users\SUDIPTO\PycharmProjects\bot project\project1\" for going to the directory
# python -m unittest GoogleSearchTest.py #likhle tobei cmd te eai file ta run hobe
# if __name__ == '__main__': #eta korle tobei cmd te flag use korte hobe  na
#     unittest.main()
# cmd open kore likhte hobe "python GoogleSearchTest.py"

#pip install html-testRunner
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/SUDIPTO/PycharmProjects/bot project/project1/reports")) #eai directory te report file create hoia jabe