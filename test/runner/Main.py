# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: Main.py
@time: 2024/4/9 13:01
"""
import time
import os.path
import smtplib
import sys
import unittest

from XTestRunner import HTMLTestRunner


class Main():

    def get_all_case(self):
        case_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "case"))
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        print(discover)
        return discover

    def set_report(self, all_case, report_path=None):
        if report_path is None:
            report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "report"))
        else:
            report_path = report_path
        title = u"TYNAM 后台管理系统"
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}'.format(y='年', m='月', d='日', h='时', M='分', s='秒'))
        report_name = os.path.join(report_path, now + "_report.html")
        with open(report_name, "wb") as report:
            runner = HTMLTestRunner(stream=report, title=title, description="测试结果", language="zh-CN")
            runner.run(all_case)
            runner.send_email(
                user="defu_wei@foxmail.com",
                password="mwmyyalzspanbfce",
                host="smtp.qq.com",
                to="15172383557@163.com",
                attachments=report_name,
                ssl=False
            )

    def run_case(self, report_path=None):
        all_case = self.get_all_case()
        self.set_report(all_case, report_path)


if __name__ == '__main__':
    Main().run_case()
    print(sys.path)
    smtplib.SMTP()
