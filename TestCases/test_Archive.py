import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def test1():

    # Page Objects

    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "//*[@id='kc-form-login']/button/div"
    link_project_xpath = "//span[@class='sub-item-text mm-text--body-bold']"
    link_dataset_xpath = "//span[@class='ms-0 ng-binding ng-scope']"
    button_open_xpath = "//span[@class='open-btn-padding ng-scope']"
    button_transform_xpath = "//span[normalize-space()='Transform']"
    option_applyFilter_xpath = "//label[normalize-space()='Apply Filter']"
    dropdown_selectColumn_xpath = "//span[@class='ui-select-placeholder text-muted ng-binding']"
    searchbox_selectColumn_xpath = "//input[@placeholder='Select a column']"
    option_selectColumn_xpath = "//span[@class='ui-select-highlight']"
    textbox_transactionType_xpath = "/html/body/div[3]/section/div/include-dataview-page/div[3]/div[6]/form/div[2]/div[1]/filter-condition/ng-include/div[2]/div/div/div/condition-line/ng-include/div[4]/div/div"
    searchbox_transactionType_xpath = "/html/body/div[3]/section/div/include-dataview-page/div[3]/div[6]/form/div[2]/div[1]/filter-condition/ng-include/div[2]/div/div/div/condition-line/ng-include/div[4]/div/div/input"
    button_apply_xpath = "//div[@type='submit']"
    button_pipelineTasks_xpath = "//button[@class ='action-bar-button d-flex-col mm-rounded-borders p-x-3 p-y-2 action-bar-button--pipeline action-bar-button--activated']"
    text_task_xpath = "//*[@id='1']/div"
    textbox_search_xpath = "//input[@placeholder='Search']"
    option_filter_xpath = "//label[@class='flex-grow-1 cursor-pointer']"
    column_quantity_xpath = "//span[normalize-space()='Quantity']"
    settings_quantityColumn_xpath = "/html[1]/body[1]/div[3]/section[1]/div[1]/include-dataview-page[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[9]/div[3]/div[2]/button[1]/div[1]/*[name()='svg'][1]"
    dropdown_sorting_xpath = "//div[@class = 'v-select__selections']/input[@placeholder = 'Select Sorting']"
    option_descending_xpath = "//div[contains(text(),'Descending')]"

    # Function Logic

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.get("https://bangalore.mammoth.io")
    driver.find_element(By.ID, textbox_username_id).send_keys("mayuri.waghmode99@gmail.com")
    driver.find_element(By.ID, textbox_password_id).send_keys("HFSCB@75qaz")
    driver.find_element(By.XPATH, button_login_xpath).click()
    driver.implicitly_wait(20)
    print(driver.title)
    driver.find_element(By.XPATH, link_project_xpath).click()
    driver.find_element(By.XPATH, link_dataset_xpath).click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, button_open_xpath).click()
    driver.implicitly_wait(10)

    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(30)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)
    print(driver.title)
    transform_option = driver.find_element(By.XPATH, button_transform_xpath)
    driver.execute_script("arguments[0].click();", transform_option)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, textbox_search_xpath).send_keys("Apply Filter")
    driver.find_element(By.XPATH, option_applyFilter_xpath).click()

    time.sleep(5)

    # Apply Filter
    driver.find_element(By.XPATH, dropdown_selectColumn_xpath).click()
    driver.find_element(By.XPATH, searchbox_selectColumn_xpath).send_keys("Transaction Type (text)")
    driver.find_element(By.XPATH, option_selectColumn_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, textbox_transactionType_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, searchbox_transactionType_xpath).send_keys("sale")
    driver.find_element(By.XPATH, searchbox_transactionType_xpath).send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, button_apply_xpath).click()
    time.sleep(30)
    # Verify PipeLine Task

    if driver.find_element(By.XPATH, text_task_xpath):
        print("true")
    else:
        print("false")
    driver.find_element(By.XPATH, button_pipelineTasks_xpath).click()

    # Sort the Column Quantity data
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, settings_quantityColumn_xpath).click()
    sorting = driver.find_element(By.XPATH, dropdown_sorting_xpath)
    driver.execute_script("arguments[0].click();", sorting)
    driver.find_element(By.XPATH, option_descending_xpath).click()

    time.sleep(20)

    # Get top 3 saling cashiers

    rank_1 = driver.find_element(By.XPATH, "//div[@role = 'rowgroup']/div[@row-id = '0']/div[@col-id='column_4']").text
    print(f"Rank 1 is {rank_1}")
    rank_2 = driver.find_element(By.XPATH, "//div[@role = 'rowgroup']/div[@row-id = '1']/div[@col-id='column_4']").text
    print(f"Rank 2 is {rank_2}")
    rank_3 = driver.find_element(By.XPATH, "//div[@role = 'rowgroup']/div[@row-id = '2']/div[@col-id='column_4']").text
    print(f"Rank 3 is {rank_3}")



