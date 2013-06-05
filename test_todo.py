import time
from selenium import webdriver

def test_simple():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(5)
    assert driver.title == 'TODO List'
    driver.quit()
