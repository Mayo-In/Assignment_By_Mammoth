import time

import pytest
from PageObjects.GetTop3CashierbySale import NavigateToTheDataSet
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class TestTask1:
    url = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_task1(self,setup):
        # Login to the Mammoth.io
        self.logger.info("*********** Login Function ***********")
        self.logger.info("Task : Login in to the Test Application")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        time.sleep(10)

        if self.driver.title == "Home | mayuri.waghmode99@gmail.com | Mammoth Testing":
            assert True
            self.logger.info("Pass: Successfully Logged into the Application.")
        else:
            self.driver.save_screenshot(".//Screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error("Fail: Failed to login into the Application.")
            assert False

        # Navigate To the Test Data Set
        self.logger.info("*********** Navigate to the Data Set ***********")
        self.logger.info("Task : Navigate to the created Test Data Set Project.")

        self.dataSet = NavigateToTheDataSet(self.driver)
        self.dataSet.NavigateToTheDataSet()

        if self.driver.title == "Store_Transactions.csv - View 1 | mayuri.waghmode99@gmail.com | Mammoth Testing":
            assert True
            self.logger.info("Pass: Successfully Navigated to the Test Data Set.")
        else:
            self.driver.save_screenshot(".//Screenshots" + "test_DataSet.png")
            self.driver.close()
            self.logger.error("Fail: Failed to Navigated to the Test Data Set.")
            assert False

        # Apply the filter
        self.logger.info("*********** Apply Filter to the Data Set ***********")
        self.logger.info("Task : Apply required filter to the created Test Data Set Project.")

        self.dataSet.ApplyFilter()
        flag = self.dataSet.verifyPiplineTask()

        if flag:
            assert True
            self.logger.info("Pass: Successfully applied filter on the Data Set.")

        else:
            self.driver.save_screenshot(".//Screenshots" + "test_applyFilter.png")
            self.logger.error("Fail: Failed to apply the filter.")
            assert False

        # Sort the Table and get the top 3 Performer
        self.logger.info("*********** Get Top 3 selling Cashiers ***********")
        self.logger.info("Task : Get top 3 Cashier names who sold maximum quantities of items.")

        self.dataSet.sortTheQuantityTable()

        for i in range(1,4):
            print(f"Rank {i} : ", self.dataSet.getTheCashierName(i))

