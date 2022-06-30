"""用于创建json文件对象"""
import json
from typing import Any
from __future__ import annotations

from .settings_file_object import SettingsFileObject


class JsonSettingsFileObject(SettingsFileObject):
    """json类型的文件对象"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "json",
    ):
        """读取一个文件, 初始化文件对象

        :param settings_dir_path: 设置文件所在的目录
        :type settings_dir_path: str
        :param settings_file_name: 设置文件的名称, 默认为"settings"
        :type settings_file_name: str
        :param settings_file_format: 设置文件的后缀, 默认为"json"
        :type settings_file_format: str
        """
        super().__init__(settings_dir_path, settings_file_name, settings_file_format)
        try:
            with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
                json.load(f)
        except json.decoder.JSONDecodeError:
            with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
                f.write("{}")

    def add(self, key: str, value: Any = None) -> JsonSettingsFileObject:
        """添加一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: JsonSettingsFileObject
        """
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            json.dump(
                settings_dict, f, sort_keys=True, indent=4, separators=(",", ": ")
            )
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
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            settings_dict = json.load(f)
        return settings_dict

    def delete(self, key: str) -> JsonSettingsFileObject:
        """删除一项配置

        :param key: 键
        :type key: str
        :return: 链式调用, 返回本身
        :rtype: JsonSettingsFileObject
        :raises KeyError: 没有这个键
        """
        super().delete(key)
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict.pop(key)
            json.dump(
                settings_dict, f, sort_keys=True, indent=4, separators=(",", ": ")
            )
        return self

    def modify(self, key: str, value: Any) -> JsonSettingsFileObject:
        """修改一项配置

        :param key: 键
        :type key: str
        :param value: 值
        :type value: Any
        :return: 链式调用, 返回本身
        :rtype: JsonSettingsFileObject
        :raises keyError: 没有这个键
        """
        super().modify(key, value)
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            json.dump(
                settings_dict, f, sort_keys=True, indent=4, separators=(",", ": ")
            )
        return self

    def exists(self, key: str) -> bool:
        """检查一个键是否存在

        :param key: 键
        :type key: str
        :return: 存在为True, 不存在为False
        :rtype: bool
        """
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            is_exists = key in json.load(f)
        return is_exists
