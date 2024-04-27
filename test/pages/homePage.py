# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: homePage.py
@time: 2022/8/28 17:47
"""
from time import sleep

from poium import Element
from selenium.webdriver.common.by import By

from test.common.tableOperation import TableOperation
from test.pages.loginPage import LoginPage


class HomePage(LoginPage):
    """主页页面"""

    # 定义search_input_element变量，表示搜索输入框元素
    search_input_element = Element("#search-input")
    # 定义search_button_element变量，表示搜索按钮元素
    search_button_element = Element(".search")
    add_button_element = Element("#add")
    edit_button_element = Element("#edt")
    delete_button_element = Element("#del")
    edit_code_element = Element("#add-dialog .code")
    edit_name_element = Element("#add-dialog .name")
    edit_sex_element = Element("#add-dialog .sex")
    edit_grader_element = Element("#add-dialog .grader")
    edit_confirm_button_element = Element("#add-dialog #confirm")
    edit_cancel_button_element = Element("#add-dialog #cancel")
    edit_dialog_element = Element("#add-dialog")
    del_confirm_button_element = Element("#del-dialog #confirm")
    del_cancel_button_element = Element("#del-dialog #cancel")

    # # 检索
    # def search_input_element(self):
    #     """检索输入框"""
    #     return self.find_element(By.ID, "search-input")
    #
    # def search_button_element(self):
    #     """检索按钮"""
    #     return self.find_element(By.CLASS_NAME, "search")
    #
    # # 按钮
    # def add_button_element(self):
    #     """新增按钮"""
    #     return self.find_element(By.ID, "add")
    #
    # def edit_button_element(self):
    #     """编辑按钮"""
    #     return self.find_element(By.ID, "edt")
    #
    # def delete_button_element(self):
    #     """删除按钮"""
    #     return self.find_element(By.ID, "del")
    #
    # # 编辑弹窗
    # def edit_code_element(self):
    #     """学好输入框"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog .code")
    #
    # def edit_name_element(self):
    #     """姓名输入框"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog .name")
    #
    # def edit_sex_element(self):
    #     """性别输入框"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog .sex")
    #
    # def edit_grader_element(self):
    #     """年级输入框"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog .grader")
    #
    # def edit_confirm_button_element(self):
    #     """编辑确定按钮"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog #confirm")
    #
    # def edit_cancel_button_element(self):
    #     """编辑取消按钮"""
    #     return self.find_element(By.CSS_SELECTOR, "#add-dialog #cancel")
    #
    # # 删除弹窗
    # def del_confirm_button_element(self):
    #     """删除确定按钮"""
    #     return self.find_element(By.CSS_SELECTOR, "#del-dialog #confirm")
    #
    # def del_cancel_button_element(self):
    #     """删除取消按钮"""
    #     return self.find_element(By.CSS_SELECTOR, "#del-dialog #cancel")

    # 页面操作方法
    def search(self, text):
        self.search_input_element.clear()
        self.search_input_element.send_keys(text)
        self.search_button_element.click()

    def edit_dialog(self, code=None, name=None, sex=None, grader=None, button="确定"):
        """编辑弹窗操作"""
        if code is not None:
            self.edit_code_element.clear()
            self.edit_code_element.send_keys(code)

        if name is not None:
            self.edit_name_element.clear()
            self.edit_name_element.send_keys(name)

        if sex is not None:
            self.edit_sex_element.clear()
            self.edit_sex_element.send_keys(sex)

        if grader is not None:
            self.edit_grader_element.clear()
            self.edit_grader_element.send_keys(grader)

        if button == "确定":
            self.edit_confirm_button_element.click()
        elif button == "取消":
            self.edit_cancel_button_element.click()
        else:
            print("编辑弹窗中按钮只能是确认和取消")

    def add_data(self, code, name, sex=None, grader=None, button="确定"):
        """
        由于code、name为必填项，所以一定要接受参数
        但sex、grade为必填项， 所以可以不用传值， 默认参数设置为None
        :param code: 学好，必填项
        :param name: 姓名，必填项
        :param sex: 性别，非必填
        :param grade: 年纪，非必填
        :param button: 新增时按钮一般都是确认按钮，所以按钮的默认值传入确定
        :return:
        """
        self.add_button_element.click()
        self.edit_dialog(code, name, sex, grader, button)

    def edit_data(self, header_text, row_text, code=None, name=None, sex=None, grader=None, button="确定"):
        """编辑数据"""
        # 使用row_click()方法是为了直接选择要编辑的单据
        TableOperation(self.driver).row_click(header_text, row_text)
        self.edit_button_element.click()
        self.edit_dialog(code, name, sex, grader, button)

    def delete_data(self, header_text, row_text, button="确定"):
        """删除数据"""
        # 使用row_click()方式是为了直接选择要删除的数据
        TableOperation(self.driver).row_click(header_text, row_text)
        self.delete_button_element.click()
        if button == "确定":
            self.del_confirm_button_element.click()
        elif button == "取消":
            self.del_cancel_button_element.click()
        else:
            print("删除弹窗中按钮只能是确定和取消")


if __name__ == '__main__':
    home = HomePage()
    home.login()
    home.add_data('1001', "张三")
    home.search("张三")
    home.edit_data('姓 名', '张三', name="李四")
    home.search("李四")
    home.delete_data("姓 名", "李四")

    sleep(3)
    home.quit_driver()
    
