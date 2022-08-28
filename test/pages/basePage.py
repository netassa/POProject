# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: basePage.py
@time: 2022/8/7 20:39
"""
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.readConfig import ReadConfig


class BasePage:
    """基础页面"""

    def __init__(self, driver=None, base_url=None):
        """
        基础的参数，webdriver、默认访问的url
        :param driver: 浏览器驱动
        :param base_url: 默认打开的url，一般是登录页面
        """

        if driver is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            driver_path = current_path + "/../../drivers/chromedriver.exe"
            self.driver = webdriver.Chrome(driver_path)
        else:
            self.driver = driver

        if base_url is None:
            self.base_url = ReadConfig.read_json("../../config/base_data.json")['base_url']
        else:
            self.base_url = base_url

        self.driver.implicitly_wait(5)
        # 设置默认打开的页面
        self.open_page()

    def open_page(self):
        """打开默认页面"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()

    def find_element(self, by, element):
        """返回单个定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alert(self):
        """返回弹窗页面"""
        sleep(1)
        return self.driver.swtich_to.alert

    def select_menu(self, menu_text):
        """菜单选择"""
        sleep(1)
        menus_element = self.driver.find_elements(By.CSS_SELECTOR, "#menu>div>h4")
        for menu in menus_element:
            if menu.text.replace(" ", "") == menu_text.replace(" ", ""):
                return menu.click()
        print(menu_text + "未找到")
        return

    def log_out(self):
        """退出登录"""
        return self.select_menu("退出登录")
