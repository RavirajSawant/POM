import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
import loginpage
option = Options()
option.add_argument('--disable-notifications')
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe",chrome_options=option)
        cls.driver.get("https://www.air.irctc.co.in/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        time.sleep(5)
    def test_login(self):
        driver = self.driver
        login = loginpage.loginpage(driver)
        login.ct_login()
        login.username("shrinisen")
        login.password("Sr23ss23@")
        login.click_login()
        time.sleep(2)
        driver.close()
    @classmethod
    def tearDownClass(cls):
        print("Login completed")
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))




