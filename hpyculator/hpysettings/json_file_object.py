"""用于创建json文件对象"""
import json
from typing import Any

from .settings_file_object import SettingsFileObject


class JsonSettingsFileObject(SettingsFileObject):
    """json类型的文件对象"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "json",
    ):
        """
        读取一个文件，初始化文件对象

        :param str settings_dir_path: 设置文件目录
        :param str settings_file_name: 设置文件名
        :param str settings_file_format: 设置文件后缀
        """
        super().__init__(settings_dir_path, settings_file_name, settings_file_format)
        try:
            with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
                json.load(f)
        except json.decoder.JSONDecodeError:
            with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
                f.write("{}")

    def add(self, key: str, value: Any = None):
        """
        添加一项配置

        :param str key: 键
        :param Any value: 值
        :return: self
        """
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            json.dump(
                settings_dict, f, sort_keys=True, indent=4, separators=(",", ": ")
            )
        return self

    def read(self, key: str) -> Any:
        """
        读取一项配置

        :param str key: 键
        :return: value 值
        :rtype: Any
        :raises keyError: 没有这个键
        """
        super().read(key)
        settings_dict = self.readAll()
        return settings_dict[key]

    def readAll(self) -> dict:
        """
        读取全部的

        :return: key-value
        :rtype: dict
        """
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            settings_dict = json.load(f)
        return settings_dict

    def delete(self, key: str):
        """
        删除一项配置

        :param key: 键
        :return: self
        :raises keyError: 没有这个键
        """
        super().delete(key)
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict.pop(key)
            json.dump(
                settings_dict, f, sort_keys=True, indent=4, separators=(",", ": ")
            )
        return self

    def modify(self, key: str, value: Any):
        """
        修改一项配置

        :param key: 键
        :param value: 值
        :return: self
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
        """
        检查一个键是否存在

        :param str key: 键
        :return: 存在为True，不存在为False
        :rtype: bool
        """
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            is_exists = key in json.load(f)
        return is_exists
