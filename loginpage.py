from selenium.webdriver.common.by import By
class loginpage:
    def __init__(self,driver):

        self.driver = driver
        self.click_login_by_xpath = "//a[text()='Login']"
        self.username_by_name = "userId"
        self.password_by_name = "password"
        self.button_login_by_xpath = "//button[contains(text(),'Login')]"
    def ct_login(self):
        self.driver.find_element(by=By.XPATH, value=self.click_login_by_xpath).click()
    def username(self,username):
        self.driver.find_element(by=By.NAME, value=self.username_by_name).send_keys(username)
    def password(self,password):
        self.driver.find_element(by=By.NAME, value=self.password_by_name).send_keys(password)
    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=self.button_login_by_xpath).click()

