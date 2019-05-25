from pytest import fixture
from selenium import webdriver

'''Це декоратор оначає, що будь-яка функція в поточному або вложеному каталозі 
з параметром hrome_brawser отримає на вхід об'єкт browser, який можна використати
без повторного його сворення методом webdriver.Chrome(r'c:\chromedriver.exe') '''
@fixture(scope='function') 
def chrome_browser():
	browser = webdriver.Chrome(r'c:\chromedriver.exe')
	return browser