# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: tabOperation.py
@time: 2022/8/7 20:22
"""
from time import sleep

from selenium.webdriver.common.by import By

from test.common.elementIsExist import ElementIsExist


class TabOperation():
    """Tab操作"""

    def __init__(self, driver):
        self.driver = driver

    def get_all_tab(self):
        """获取所有的tab"""
        sleep(1)

        # 获取所有的tab父元素
        # 元素定位，我们默认取CSS定位
        fathers_tabs = [['.tabs1', 'a2'],
                        ['.tabs', 'a']]

        # 获取页面显示父节点下的所有tab
        for father_tab in fathers_tabs:
            # 使用is_exist()方法判断父节点是否存在，如果父节点不存在，则查找的tab不匹配
            father_exist = ElementIsExist(self.driver).is_exist(father_tab)
            if father_exist:
                father = self.driver.find_element(By.CSS_SELECTOR, father_tab[0])
                tabs = father.find_element(By.CSS_SELECTOR, father_tab[1])
                return tabs

    def switch_tab(self, tab_text):
        """
        切换tab
        :param tab_text:需要切换到的tab内容
        :return:
        """
        tabs = self.get_all_tab()
        for tab in tabs:
            if tab.text == tab_text:
                tab.click()
                return
