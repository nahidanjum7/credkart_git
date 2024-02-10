import pytest
from selenium import webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


##creating a hookup function
#comment liner
def pytest_addoption(parser):
    parser.addoption("--browser") #by this browser is now recognized to your python/pytest

# pytest -v --html=HtmlReports/newreport.html --browser chrome

@pytest.fixture
def setup(request):
    browser=request.config.getoption("--browser") #this browser argument will get value for browser eg.chrome,firefox,edge

    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser == "edge":
        driver=webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome(options=chrome_options)


    # driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://automation.credence.in/login")
    yield driver
    driver.quit()

