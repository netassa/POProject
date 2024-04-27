# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: test3.py
@time: 2024/4/9 18:03
"""
import os
import unittest
from XTestRunner import HTMLTestRunner

class TestEmail(unittest.TestCase):
    """测试用例说明"""

    def test_success(self):
        print("你好，世界！")
        self.assertEqual(2 + 3, 5)

    @unittest.skip("skip case")
    def test_skip(self):
        pass

    def test_fail(self):
        self.assertEqual(5, 6)

    def test_error(self):
        self.assertEqual(a, 6)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        TestEmail("test_success"),
        TestEmail("test_skip"),
        TestEmail("test_fail"),
        TestEmail("test_error")
    ])
    report = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../report/email_result.html"))
    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试发送邮件',
            tester='虫师',
            description=['类型：测试发送邮件'],
            language="zh-CN"
        )
        runner.run(suit)
        runner.send_weixin(
            access_token="4ef6b1f9-8cc0-4ab0-847b-00d92cd5f328",
            at_mobiles=[15172383557, 18124140914],
            is_at_all=True
        )


        # 发送邮件方式 1：send_email()方法
        # runner.send_email(
        #     user="15172383557@163.com",
        #     password="QPUAGKMZIDHSVVVV",
        #     host="smtp.163.com",
        #     port=587,
        #     to="defu_wei@foxmail.com",
        #     attachments=report,
        #     ssl=True
        # )
    # # 发送方式 2：SMTP类
    # smtp = SMTP(user="15172383557@163.com", password="QPUAGKMZIDHSVVVV", host="smtp.163.com", ssl=False)
    # smtp.sender(to="defu_wei@foxmail.com", subject="XTestRunner测试邮件", attachments=report)