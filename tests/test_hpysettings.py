import os
import random
import time

from . import hpysettings

# 测试数据
setting_file_path = os.path.join(os.getcwd(), "settings_file_dir", str(time.time_ns()))
test_text = random.randint(0, 9999)
test_key = str(random.randint(0, 9999)) + str("test_key")
test_key2 = str(random.randint(0, 9999)) + str("test_key2")
test_value = random.randint(0, 9999)
test_value2 = True
test_value3 = test_text
json_file_name = f"{test_text}.json"
yaml_file_name = f"{test_text}.yaml"
toml_file_name = f"{test_text}.toml"


# 创建文件实例
instance_json_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name=json_file_name.split(".")[0],
    settings_file_format=json_file_name.split(".")[1],
)

instance_toml_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name=toml_file_name.split(".")[0],
    settings_file_format=toml_file_name.split(".")[1],
)

instance_yaml_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name=yaml_file_name.split(".")[0],
    settings_file_format=yaml_file_name.split(".")[1],
)


def test_settings_file():
    """
    测试文件实例

    :return: None
    """
    for instance_settings_file, file_name in (
        (instance_yaml_settings_file, yaml_file_name),
        (instance_toml_settings_file, toml_file_name),
        (instance_json_settings_file, json_file_name),
    ):
        # 测试，add read readAll
        instance_settings_file.add(test_key, test_value)
        assert test_value == instance_settings_file.read(test_key)
        assert {test_key: test_value} == instance_settings_file.readAll()

        # 测试，modify read readAll
        instance_settings_file.modify(test_key, test_value2)
        assert test_value2 == instance_settings_file.read(test_key)
        assert {test_key: test_value2} == instance_settings_file.readAll()

        # 测试，delete add exists
        instance_settings_file.delete(test_key)
        instance_settings_file.add(test_key, test_value3)
        assert instance_settings_file.exists(test_key) is True

        # 测试，setting_file_path
        assert instance_settings_file.setting_file_path == os.path.join(
            setting_file_path, file_name
        )

        # 测试读取不存在的键
        try:
            instance_settings_file.read(test_key2)
            # pytest.fail("读取不存在的键时未能引发KeyError错误")
        except KeyError:
            ...

        # 测试删除不存在的键
        try:
            instance_settings_file.delete(test_key2)
            # pytest.fail("删除不存在的键时未能引发KeyError错误")
        except KeyError:
            ...

        # 测试修改不存在的键
        try:
            instance_settings_file.modify(test_key2, test_value)
            # pytest.fail("修改不存在的键时未能引发KeyError错误")
        except KeyError:
            ...
