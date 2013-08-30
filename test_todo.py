import time
from selenium import webdriver
import pytest


class TestTODO(object):

    def no_test_simple(self, resource_handler):
        driver = resource_handler.driver
        time.sleep(2)
        assert driver.title == 'TODO List'
        driver.close()
        driver.quit()

    def test_add_new_item(self, resource_handler):
        driver = resource_handler.driver
        time.sleep(2)
        from page import MainPage
        main_page = MainPage(resource_handler)
        main_page.click_new_task_link()

        #element = driver.find_element_by_name("task")
        #element.send_keys("Learn Webdriver")

        main_page.task_element = "Learn Webdriver 2"

        element = driver.find_element_by_name("save")
        element.click()
        time.sleep(2)
        driver.close()
        driver.quit()




def no_test_edit_item():
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
