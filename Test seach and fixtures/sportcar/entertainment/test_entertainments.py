# from selenium import webdriver
from pytest import mark

@mark.entertaintments
@mark.ui
def test_entertaintments_to_browser(chrome_browser):
    # browser = webdriver.Chrome(r'c:\chromedriver.exe')
    chrome_browser.get('https://www.carfax.eu/')
    assert True