# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: aboutPage.py
@time: 2022/8/28 18:40
"""
from time import sleep

from poium import Element
from selenium.webdriver.common.by import By

from test.pages.loginPage import LoginPage


class AboutPage(LoginPage):
    """关于我们页面"""

    about_element = Element("#about h1")
    # def about_element(self):
    #     """关于我们页面判断元素"""
    #     return self.find_element(By.CSS_SELECTOR, "#about h1")

if __name__ == '__main__':
    about = AboutPage()
    about.login()
    about.select_menu("关于我们")
    assert about.about_element.is_displayed()
    about.log_out()
    sleep(3)
