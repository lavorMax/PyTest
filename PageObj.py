from selenium import webdriver

class Page:
    def __init__(self, browser, url):
        browser.get("https://www.work.ua/")
        self.browser = browser
        print(self.browser)
        
    def getSearchForm(self):
        return self.browser.find_element_by_css_selector('#search')
    
    def getMainSearchLabel(self):
        return self.browser.find_element_by_css_selector('h1.text-basic.text-muted')
    
    def getCityMenu(self):
        return self.browser.find_element_by_css_selector("#city")
    
    def getDaysSort(self):
        return self.getMainSearchLabel().find_element_by_css_selector(".glyphicon.glyphicon-chevron-down.glyph-indent")
    
    def get7DaysSort(self):
        return self.browser.find_element_by_css_selector('[data-days="123"]')
    
    def getCreatedBeforeInRes(self):
        return self.browser.find_element_by_css_selector('.text-muted.small')
    