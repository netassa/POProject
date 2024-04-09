# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: loginPage.py
@time: 2022/8/28 17:12
"""
import os.path
from time import sleep

from selenium.webdriver.common.by import By

from test.pages.basePage import BasePage
from utils.readConfig import ReadConfig
from poium import Page, Element, Elements


class LoginPage(BasePage, Page):
    """登录页面"""
    email_element = Element(class_name="email")
    password_element = Element(class_name="password")
    login_button = Element(".login-btn>input[value='登  录']")
    email_error_element = Element(".email+div.msg")
    password_error_element = Element(".password+div.msg")

    # def email_element(self):
    #     """邮箱地址"""
    #     return self.find_element(By.CLASS_NAME, "email")
    #
    # def password_element(self):
    #     """密码"""
    #     return self.find_element(By.CLASS_NAME, "password")
    #
    # def login_button(self):
    #     """登录"""
    #     return self.find_element(By.CSS_SELECTOR, ".login-btn>input[value='登  录']")
    #
    # def email_error_element(self):
    #     """邮箱地址错误"""
    #     return self.find_element(By.CSS_SELECTOR, ".email+div.msg")
    #
    # def password_error_element(self):
    #     """密码错误"""
    #     return self.find_element(By.CSS_SELECTOR, ".password+div.msg")
    #
    # def login_fail_element(self):
    #     """登录失败"""
    #     return self.switch_alert()

    def login(self, email=None, password=None):
        """登录操作"""
        account_email, account_password = self.get_account()

        if email is None:
            email = account_email
        else:
            email = email

        if password is None:
            password = account_password
        else:
            password = password

        self.email_element.send_keys(email)
        self.password_element.send_keys(password)
        self.login_button.click()

    def get_account(self):
        """获取默认邮箱地址和密码"""
        account = ReadConfig().read_json(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'base_data.json')))
        return account['email'], account['password']


if __name__ == "__main__":
    p = LoginPage()
    p.login()
    p.switch_to_alert().accept()
    sleep(5)
    p.quit_driver()
