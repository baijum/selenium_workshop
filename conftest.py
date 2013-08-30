import pytest

from selenium import webdriver
from testconfig import general_config


class ResourceHandler(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(general_config['base_url'])

    def release(self):
        pass


def _release_resource_handler(handler):
    """teardown resource_handler"""
    handler.release()

def _get_resource_handler():
    """Factory for resource_handler"""
    resource_handler = ResourceHandler()
    return resource_handler


@pytest.fixture
def resource_handler(request):
    """Create resource_handler funcarg"""
    return request.cached_setup(
        setup=_get_resource_handler,
        teardown=_release_resource_handler,
        scope='function')
