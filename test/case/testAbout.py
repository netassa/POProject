import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from test.pages.aboutPage import AboutPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # driver_path = os.path.abspath(
        #     os.path.join(os.path.dirname(__file__), '..', '..', 'drivers', 'chromedriver.exe'))
        # service = webdriver.ChromeService(executable_path=driver_path)
        # cls.driver = webdriver.Chrome(service=service)
        cls.about = AboutPage()
        cls.about.login()

    @classmethod
    def tearDownClass(cls):
        cls.about.quit_driver()

    def test_about01(self):
        # 点击关于我们菜单
        self.about.select_menu("关于我们")
        # 获取关于我们元素
        about = self.about.about_element
        # 断言获取到的文本是否为关于我们
        self.assertEqual("关于我们", about.text)  # add assertion here

    # def test_about02(self):
    #     self.driver.get("https://www.baidu.com")
    #     self.driver.find_element(By.ID, "test")


if __name__ == '__main__':
    unittest.main()
