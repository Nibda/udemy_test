from selenium import webdriver
from pytest import mark

@mark.entertaintments
@mark.ui
def test_entertaintments_tobrowser():
    browser = webdriver.Chrome(r'c:\chromedriver.exe')
    browser.get('https://www.carfax.eu/')
    assert True