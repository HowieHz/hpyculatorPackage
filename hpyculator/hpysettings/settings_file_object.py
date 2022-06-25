import os
from abc import ABC, abstractmethod
from typing import Any


class SettingsFileObject(ABC):
    """设置文件的基类，要新支持一种格式就继承这个抽象类"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "",
    ):
        """
        读取一个文件laod

        :param str settings_dir_path: 设置文件目录
        :param str settings_file_name: 设置文件名
        :param str settings_file_format: 设置文件猴嘴
        """
        self._setting_dir_path = settings_dir_path

        # 检查存放设置文件的文件夹是否存在
        if not os.path.exists(self._setting_dir_path):
            os.makedirs(self._setting_dir_path)

        # 初始化设置文件位置
        self._settings_file_path = str(
            os.path.join(
                settings_dir_path, f"{settings_file_name}.{settings_file_format}"
            )
        )

        # 初始化文件
        self._settings_file_stream = open(
            self._settings_file_path, mode="a+", encoding="utf-8"
        )
        self._settings_file_stream.close()

    @abstractmethod
    def add(self, key: str, value: Any):
        """
        添加一项配置

        :param str key: 键
        :param Any value: 值
        :return: self
        """

    @abstractmethod
    def read(self, key: str):
        """
        读取一项配置

        :param str key: 键
        :return: value 值
        :rtype: Any
        :raises keyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def readAll(self):
        """
        读取全部的

        :return: key-value
        :rtype: dict
        """

    @abstractmethod
    def delete(self, key: str):
        """
        删除一项配置

        :param key: 键
        :return: self
        :raises keyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def modify(self, key: str, value: Any):
        """
        修改一项配置

        :param key: 键
        :param value: 值
        :return: self
        :raises keyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def exists(self, key: str) -> bool:
        """
        检查一个键是否存在

        :param str key: 键
        :return: 存在为True，不存在为False
        :rtype: bool
        """
        return False

    @property
    def setting_file_path(self) -> str:
        """
        设置文件的路径

        :return: 设置文件的路径
        :rtype: str
        """
        return self._settings_file_path
