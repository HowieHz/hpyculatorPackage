"""管理设置文件"""
# xml X
# ini X

from .toml_file_object import TomlSettingsFileObject
from .json_file_object import JsonSettingsFileObject
from .yaml_file_object import YamlSettingsFileObject

import os

dict_settings_file_object = {
    "toml": TomlSettingsFileObject,
    "json": JsonSettingsFileObject,
    "yaml": YamlSettingsFileObject,
}

def load(
    settings_dir_path: str = "",
    settings_file_name: str = "settings",
    settings_file_format: str = "toml",
):
    """
    加载一个设置文件对象
    工厂函数

    :param settings_dir_path: 设置文件所在目录
    :param settings_file_name: 设置文件的文件名
    :param settings_file_format: 设置文件的类型（后缀）
    :return:
    """
    if not settings_dir_path:
        settings_dir_path = str(os.path.join(os.getcwd(), "Setting"))  # 初始化设置目录
    return dict_settings_file_object[settings_file_format](
        settings_dir_path, settings_file_name, settings_file_format
    )
    # settings_dir_path = self._settings_dir_path  # 易于语法高亮
    # return JsonSettingsFileObject(settings_dir_path,
    #                               settings_file_name,
    #                               settings_file_format)
