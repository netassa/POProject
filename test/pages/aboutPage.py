# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: aboutPage.py
@time: 2022/8/28 18:40
"""
from selenium.webdriver.common.by import By

from test.pages.loginPage import LoginPage


class AboutPage(LoginPage):
    """关于我们页面"""

    def about_element(self):
        """关于我们页面判断元素"""
        return self.find_element(By.CSS_SELECTOR, "#about h1")
