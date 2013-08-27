import time
from selenium import webdriver

def test_simple():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(5)
    assert driver.title == 'TODO List'
    driver.close()
    driver.quit()

def test_add_new_item():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(2)
    element = driver.find_element_by_link_text('New')
    element.click()
    element = driver.find_element_by_name("task")
    element.send_keys("Learn Webdriver")
    element = driver.find_element_by_name("save")
    element.click()
    time.sleep(2)
    driver.close()
    driver.quit()

def test_edit_item():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/')
    time.sleep(2)
    element = driver.find_element_by_xpath("//a[@href='edit/1']")
    element.click()
    time.sleep(2)
    select_element = driver.find_element_by_xpath("//select[@name='status']")
    all_options = select_element.find_elements_by_tag_name("option")
    for option in all_options:
        if option.text == 'closed':
            option.click()
    element = driver.find_element_by_name("save")
    element.click()
    time.sleep(2)
    driver.close()
    driver.quit()
