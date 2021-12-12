import pytest
import time
from PageObj import Page
from selenium.webdriver.common.keys import Keys
import allure
    
@allure.suite("City form result test")
@allure.story("test suit for lab 5")      
def test_searchFormTest(browser):
    search_string = "C#"
    
    with allure.step("finding " + search_string):
        search_form = pytest.page.getSearchForm()
        search_form.send_keys(search_string)
        search_form.send_keys(Keys.RETURN)
        
    with allure.step("Checking main lanel after sarch"):    
        actual_result = pytest.page.getMainSearchLabel().text
        assert search_string in actual_result


@allure.suite("City form result test")
@allure.story("test suit for lab 5")
def test_cityFormTest(browser):
    with allure.step("finding Дніпро vacancies"):
        city_form = pytest.page.getCityMenu()
        city_form.clear()
        city_form.send_keys("Дніпро")
        pytest.page.getSearchForm().send_keys(Keys.RETURN)
        time.sleep(1)
        
    with allure.step("Checking main label after search"):
        
        actual_value = pytest.page.getMainSearchLabel().text
                     
        assert "Дніпр" in actual_value
                         
                                               
@allure.suite("Check sorting by date")
@allure.story("test suit for lab 5")
def test_sortByDateTest(browser):
        
    with allure.step("sorting by date in 7 dayperiod"):
        pytest.page.getDaysSort().click()
        pytest.page.get7DaysSort().click()
        actual_value = pytest.page.getCreatedBeforeInRes().text
    
    with allure.step("Checking result if it in 7 days range"):
        sevendays = {"1","2","3","4","5","6","7"}
        result = ""
    
        for i in sevendays:
            if(i in actual_value):
                result = i
    
        assert result != ""
        