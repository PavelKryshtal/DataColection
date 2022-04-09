import pytest

from config.conftest import *
# from config.pom import StateFunctions
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestBohUpdate:

    def test_update(self):
        pass
