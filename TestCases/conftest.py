import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

# ################ pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Mammoth Assignment",
        "Module Name": "Task 1: Get Top 3 Cashiers by their Sales",
        "Tester": "Mayuri"
    }
