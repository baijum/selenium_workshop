import time
from selenium import webdriver

def test_simple():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(5)
    assert driver.title == 'TODO List'
    driver.quit()

def test_add_new_item():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(2)
    element = driver.find_element_by_link_text('New')
    element.click()
    time.sleep(2)
    driver.quit()
