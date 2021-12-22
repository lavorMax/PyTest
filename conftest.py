import pytest
from page import Page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install());
    browser.implicitly_wait(2)
    
    pytest.page = Page(browser, "https://www.work.ua/")
    
    try:
        yield browser

    finally:
        browser.quit()
        
    return browser
       

