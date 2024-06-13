import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup_class(request):
    # Class-level setup code
    logging.info("Setting up the class with DB connection code")
    yield
    # Class-level teardown code
    logging.info("Tearing down the class with DB connection closure")


@pytest.fixture
def setup_method(request, setup_class):
    # Setup method to initialize the browser before each test
    logging.info("Setting up the test case - browser open")
    serv_obj = Service(r'C:\Users\rihaa\Documents\Drivers\chromedriver.exe')
    request.cls.driver = webdriver.Chrome(service=serv_obj)
    request.cls.driver.maximize_window()
    yield
    # Teardown method to close the browser after each test
    logging.info("Tearing down the test case - browser close")
    request.cls.driver.quit()
