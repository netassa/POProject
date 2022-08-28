# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: testLogin.py
@time: 2022/8/28 20:54
"""
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from test.pages.loginPage import LoginPage


class TestLogin(unittest.TestCase):
    """登录测试"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.quit_driver()

    def test_login01(self):
        """登录成功"""
        self.login.login()
        assert self.login.find_element(By.CSS_SELECTOR, "#container>h1")


if __name__ == '__main__':
    unittest.main()
