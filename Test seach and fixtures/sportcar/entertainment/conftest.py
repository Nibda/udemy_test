from pytest import fixture
from selenium import webdriver

# @fixture(scope='function') # make test in separated browsers
@fixture(scope='session') # make test in one browser
def chrome_browser():
	browser = webdriver.Chrome(r'c:\chromedriver.exe')
	# return browser
	yield browser
	
	# teardown
	print('I am teardawn this browser')