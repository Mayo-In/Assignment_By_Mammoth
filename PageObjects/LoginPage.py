from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    # **********************************Page Objects**********************************
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "//*[@id='kc-form-login']/button/div"
    # *********************************Function Logics*********************************

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassWord(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
