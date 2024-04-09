# -*-coding:utf-8-*-

import json
import os


class ReadConfig:
    """
    读取配置文件，Excel、json等文件的读取方法都可写在此类下
    """

    def __init__(self):
        pass

    @staticmethod
    def read_json(json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                config = json.load(f)
                return config
        except IOError:
            print("文件不存在或不是json文件")


if __name__ == '__main__':
    data = ReadConfig().read_json(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'base_data.json')))
    print(data)
    print(data['base_url'], data['email'], data['password'])
