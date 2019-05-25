# from selenium import webdriver
from pytest import mark


@mark.body
class BodyTests:

    @mark.ui
    def test_to_browser(self, chrome_browser):
        # browser = webdriver.Chrome(r'c:\chromedriver.exe')
        chrome_browser.get('https://carsfromwest.com')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
