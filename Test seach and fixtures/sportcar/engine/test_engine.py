# from selenium import webdriver
from pytest import mark

@mark.engine
@mark.ui
def test_engine_funtions_to_browser(chrome_browser):
    # browser = webdriver.Chrome(r'c:\chromedriver.exe')
    chrome_browser.get('https://cargoline.com.ua')
    assert True