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


class LoginPage(BasePage):
    """登录页面"""

    def email_element(self):
        """邮箱地址"""
        return self.find_element(By.CLASS_NAME, "email")

    def password_element(self):
        """密码"""
        return self.find_element(By.CLASS_NAME, "password")

    def login_button(self):
        """登录"""
        return self.find_element(By.CSS_SELECTOR, ".login-btn>input[value='登  录']")

    def email_error_element(self):
        """邮箱地址错误"""
        return self.find_element(By.CSS_SELECTOR, ".email+div.msg")

    def password_error_element(self):
        """密码错误"""
        return self.find_element(By.CSS_SELECTOR, ".password+div.msg")

    def login_fail_element(self):
        """登录失败"""
        return self.switch_alert()

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

        self.email_element().send_keys(email)
        self.password_element().send_keys(password)
        self.login_button().click()

    def get_account(self):
        """获取默认邮箱地址和密码"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        json_path = current_path + "/../../config/base_data.json"
        account = ReadConfig().read_json(json_path)
        return account['email'], account['password']


if __name__ == "__main__":
    p = LoginPage()
    p.login()
    sleep(5)
    p.quit_driver()
