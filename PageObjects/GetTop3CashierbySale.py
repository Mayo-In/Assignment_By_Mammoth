from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class NavigateToTheDataSet:

    # **********************************Page Objects**********************************

    link_project_xpath = "//span[@class='sub-item-text mm-text--body-bold']"
    link_dataset_xpath = "//span[@class='ms-0 ng-binding ng-scope']"
    button_open_xpath = "//span[@class='open-btn-padding ng-scope']"
    button_transform_xpath = "//span[normalize-space()='Transform']"
    textbox_search_xpath = "//input[@placeholder='Search']"
    option_filter_xpath = "//label[normalize-space()='Label, Filter and Replace']"
    option_applyFilter_xpath = "//label[normalize-space()='Apply Filter']"
    dropdown_selectColumn_xpath = "//span[@class='ui-select-placeholder text-muted ng-binding']"
    textbox_transactionType_xpath = "/html/body/div[3]/section/div/include-dataview-page/div[3]/div[6]/form/div[2]/div[1]/filter-condition/ng-include/div[2]/div/div/div/condition-line/ng-include/div[4]/div/div"
    searchbox_selectColumn_xpath = "//input[@placeholder='Select a column']"
    option_selectColumn_xpath = "//span[@class='ui-select-highlight']"
    searchbox_transactionType_xpath = "/html/body/div[3]/section/div/include-dataview-page/div[3]/div[6]/form/div[2]/div[1]/filter-condition/ng-include/div[2]/div/div/div/condition-line/ng-include/div[4]/div/div/input"
    button_apply_xpath = "//div[@type='submit']"
    button_pipelineTasks_xpath = "//button[@class ='action-bar-button d-flex-col mm-rounded-borders p-x-3 p-y-2 action-bar-button--pipeline action-bar-button--activated']"
    text_task_xpath = "//*[@id='1']/div"
    cell_dataset_xpath = "//div[@row-id='0']/div[@col-id='column_4']"
    settings_quantityColumn_xpath = "/html[1]/body[1]/div[3]/section[1]/div[1]/include-dataview-page[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[9]/div[3]/div[2]/button[1]/div[1]/*[name()='svg'][1]"
    dropdown_sorting_xpath = "//div[@class = 'v-select__selections']/input[@placeholder = 'Select Sorting']"
    option_descending_xpath = "//div[contains(text(),'Descending')]"

    # *********************************Function Logics*********************************

    def __init__(self, driver):
        self.driver = driver

    def NavigateToTheDataSet(self):
        # Navigate to the DataSet created for testing purpose

        self.driver.find_element(By.XPATH, self.link_project_xpath).click()
        self.driver.find_element(By.XPATH, self.link_dataset_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.button_open_xpath).click()
        time.sleep(10)

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(30)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

    def ApplyFilter(self):
        # Applying tne filter to get the transaction type as "Sale"

        transform_option = self.driver.find_element(By.XPATH, self.button_transform_xpath)
        self.driver.execute_script("arguments[0].click();", transform_option)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.textbox_search_xpath).send_keys("Apply Filter")
        self.driver.find_element(By.XPATH, self.option_applyFilter_xpath).click()

        time.sleep(2)

        # Apply Filter
        self.driver.find_element(By.XPATH, self.dropdown_selectColumn_xpath).click()
        self.driver.find_element(By.XPATH, self.searchbox_selectColumn_xpath).send_keys("Transaction Type (text)")
        self.driver.find_element(By.XPATH, self.option_selectColumn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_transactionType_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.searchbox_transactionType_xpath).send_keys("sale")
        self.driver.find_element(By.XPATH, self.searchbox_transactionType_xpath).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.button_apply_xpath).click()
        time.sleep(15)

    def verifyPiplineTask(self):
        if self.driver.find_element(By.XPATH, self.text_task_xpath):
            self.driver.find_element(By.XPATH, self.button_pipelineTasks_xpath).click()
            return True
        else:
            return False

    def sortTheQuantityTable(self):

        self.driver.find_element(By.XPATH, self.settings_quantityColumn_xpath).click()
        sorting_option = self.driver.find_element(By.XPATH, self.dropdown_sorting_xpath)
        self.driver.execute_script("arguments[0].click();", sorting_option)
        self.driver.find_element(By.XPATH, self.option_descending_xpath).click()

        time.sleep(10)

    def getTheCashierName(self, rank):
        # Get the top 3 cashier by the quantity of their respective sales

        cashier_name = self.driver.find_element(By.XPATH,
                                     f"//div[@role = 'rowgroup']/div[@row-id = '{rank-1}']/div[@col-id='column_4']").text

        return cashier_name

