"""用于创建toml文件对象"""
from typing import Any
from __future__ import annotations

import rtoml as toml

from .settings_file_object import SettingsFileObject


class TomlSettingsFileObject(SettingsFileObject):
    """toml类型的文件对象"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "toml",
    ):
        """读取一个文件, 初始化文件对象

        :param settings_dir_path: 设置文件所在的目录
        :type settings_dir_path: str
        :param settings_file_name: 设置文件的名称, 默认为"settings"
        :type settings_file_name: str
        :param settings_file_format: 设置文件的后缀, 默认为"toml"
        :type settings_file_format: str
        """
        super().__init__(settings_dir_path, settings_file_name, settings_file_format)

    def add(self, key: str, value: Any = None) -> TomlSettingsFileObject:
        """添加一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: TomlSettingsFileObject
        """
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            f.write(toml.dumps(settings_dict))
        return self

    def read(self, key: str) -> Any:
        """读取一项配置

        :param key: 键
        :type key: str
        :return: 值
        :rtype: Any
        :raises KeyError: 没有这个键
        """
        super().read(key)
        settings_dict = self.readAll()
        return settings_dict[key]

    def readAll(self) -> dict:
        """读取全部的

        :return: 键值对
        :rtype: dict
        """
        # 等价return toml.load(self._settings_file_path)[key]
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            settings_dict = toml.loads(f.read())
        return settings_dict

    def delete(self, key: str) -> TomlSettingsFileObject:
        """删除一项配置

        :param key: 键
        :type key: str
        :return: 链式调用, 返回本身
        :rtype: TomlSettingsFileObject
        :raises KeyError: 没有这个键
        """
        super().delete(key)
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict.pop(key)
            f.write(toml.dumps(settings_dict))
        return self

    def modify(self, key: str, value: Any) -> TomlSettingsFileObject:
        """修改一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: TomlSettingsFileObject
        :raises keyError: 没有这个键
        """
        super().modify(key, value)
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            f.write(toml.dumps(settings_dict))
        return self

    def exists(self, key: str) -> bool:
        """检查一个键是否存在

        :param key: 键
        :type key: str
        :return: 存在为True, 不存在为False
        :rtype: bool
        """
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            is_exists = key in toml.loads(f.read())
        return is_exists
