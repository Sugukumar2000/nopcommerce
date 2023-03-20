from selenium import webdriver
import pytest
import sys
arg = sys.argv
print(arg)

@pytest.fixture()
def setup():
    #if arg == "chrome":
    driver = webdriver.chrome()
    return driver
    #elif arg == "firefox":
      #  driver = webdriver.firefox()
      #  return driver


#def pytest_addoption(arg): # to get value form CLI
    #arg.addoption("--browser")

#@pytest.fixture()
#def browser(request): # to return browser value
    #return request.config.getoption("--browser")

