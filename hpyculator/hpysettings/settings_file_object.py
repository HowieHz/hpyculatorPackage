import os
from abc import ABC, abstractmethod
from typing import Any
from __future__ import annotations


class SettingsFileObject(ABC):
    """设置文件的基类，要新支持一种格式就继承这个抽象类"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "",
    ):
        """读取一个文件, 初始化文件对象

        :param settings_dir_path: 设置文件所在的目录
        :type settings_dir_path: str
        :param settings_file_name: 设置文件的名称, 默认为"settings"
        :type settings_file_name: str
        :param settings_file_format: 设置文件的后缀, 默认为""
        :type settings_file_format: str
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
    def add(self, key: str, value: Any) -> SettingsFileObject:
        """添加一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: SettingsFileObject
        """

    @abstractmethod
    def read(self, key: str) -> Any:
        """读取一项配置

        :param key: 键
        :type key: str
        :return: 值
        :rtype: Any
        :raises KeyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def readAll(self):
        """读取全部的

        :return: 键值对
        :rtype: dict
        """

    @abstractmethod
    def delete(self, key: str):
        """删除一项配置

        :param key: 键
        :type key: str
        :return: 链式调用, 返回本身
        :rtype: SettingsFileObject
        :raises KeyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def modify(self, key: str, value: Any):
        """修改一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: SettingsFileObject
        :raises keyError: 没有这个键
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def exists(self, key: str) -> bool:
        """检查一个键是否存在

        :param key: 键
        :type key: str
        :return: 存在为True, 不存在为False
        :rtype: bool
        """

    @property
    def setting_file_path(self) -> str:
        """设置文件的路径

        :return: 设置文件的路径
        :rtype: str
        """
        return self._settings_file_path
